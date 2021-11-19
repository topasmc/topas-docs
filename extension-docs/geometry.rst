.. _extension_geometry:

Custom Geometry Components
==========================

.. highlight:: c++

First line of the cc file must be of the form::

    // Component for MyComponent1

TOPAS geometry components are like small pieces of what Geant4 users call their "detector construction" class. The Geometry sections of the Geant4 Application Developers Guide provide details on the full geometrical functionality of Geant4. In this section, we explain some details about how to write TOPAS components, but we assume that you are already comfortable with basic concepts of C++ and Geant4 geometry. The notes below are intended to discuss only those parts which may not be obvious.

Your geometry component class will be a concrete implementation of the base class:  TsVGeometryComponent.

You can get any parameter name of the current component by using the GetFullParmName method. For example, if your parameter file specifies:

.. code-block:: topas

    d:Ge/MyComponent/Blatz = 42. mm

``GetFullParmName("Blatz")`` will return ``Ge/MyComponent/Blatz``.
You can then feed this resulting string into the parameter access methods such as::

    G4Double blatzLength = fPm->GetDoubleParameter(GetFullParmName("Blatz"), "length");

Your component may contain any of the following methods. Careful attention to what goes where will insure that your classes are robust under 4D and the base classes will do much of the work for you.

Constructor: Must exist and may be empty.
This method will only be called at the very beginning of the simulation. It will not be called after changes in 4D. Only put things here if you are absolutely certain you will not need to recompute them during the simulation.

Destructor: Must exist and may be empty.
Destroy any special objects you created with "new" statements. You may not destroy solids, logical volumes or physical volumes. These destructions are handled for you by the base class.

You do not need to do anything to handle the basic parameters, Parent, TransX, TransY, TransZ, RotX, RotY, RotZ, Material and Color. These are handled for you by the base class, including 4D capabilities.

If there are any other parameters that you may want to vary in 4D, provide a method ``UpdateForSpecificParameterChange(G4String parameter)``.

* If the parameter name is one that you want to handle, do so. Be sure to use GetFullParmNameLower rather than GetFullParmName in your check.
* If your handing of this parameter moves a volume relative to its mother volume, advise Geant4’s smart voxel system that it needs to re-optimize the mother volume by calling  AddToReoptimizeList. The argument should be the mother’s logical volume.
* If the parameter name is not one that you want to handle, pass it on to the base class handler, TsVGeometryComponent::UpdateForSpecificParameterChange. This is essential to enable basic 4D behaviors such as overall component motion.

TsMultiLeafCollimator.cc is a good example of this kind of behavior. It allows leaf position to change over time.

For the rest of your work, provide a method Construct.

The first line of Construct MUST be::

    BeginConstruction();

The rest of Construct is whatever you want to do to create Geant4 Solids, Logical Volumes and Physical Volumes. But you must follow some rules to insure that TOPAS will be able to properly manage your volumes in 4D.

* You create Geant4 Solids just as you would in any Geant4 geometry.
* You DO NOT create Geant4 Logical Volumes or Physical Volumes directly, but instead use helper methods from the base class. This allows TOPAS to manage your solids and volumes efficiently, even if they are moving.

To create the overall logical volume for your component, use::

    fEnvelopeLog = CreateLogicalVolume(G4VSolid* solid);

The logical volume will automatically get the material and visualization properties specified in your parameter file for this component, such as Ge/MyComponent/Material and Ge/MyComponent/Color. Be sure that the value on the left side of the above is exactly "fEnvelopeLog". This insures that TOPAS knows the overall logical volume’s name and is essential for TOPAS to support your component in 4D.

If a component is made up of more than one volume, these additional volumes are called "SubComponents." A component may have more zero, one or more SubComponents. An example of SubComponents is the Blades in a Propeller, such as:

.. code-block:: topas

    s:Ge/Propeller/Type = "TsPropeller"
    ...
    i:Ge/Propeller/NbOfBlades = Ge/PropellerConstant/NbBlades
    s:Ge/Propeller/Blade/Material = "World"
    s:Ge/Propeller/Blade/Color = "skyblue"

In all of the following forms, the subComponentName argument can be either a G4String or a char*.

To create a logical volume for a subcomponent, use::

    G4LogicalVolume* CreateLogicalVolume(subComponentName, G4VSolid* solid);

TOPAS will look for material and visualization parameters such as:

.. code-block:: topas

    Ge/ComponentName/SubComponentName/Material = ...

To hard-code the material, rather than having it come from this parameter, use::

    G4LogicalVolume* CreateLogicalVolume( subComponentName, G4String& materialName, G4VSolid* solid);

This is particularly useful in cases where you want the material to be the same as the component’s mother, that is, the material surrounding your component. We do this, for example, when we want to make a void in a collimator. To get that mother volume’s material name, use::

    G4String envelopeMaterialName = fParentComponent->GetResolvedMaterialName();

The base class will take care of automatically setting your component’s visualization attributes based on the component’s parameters. But you can set different attributes for subComponents with code such as::

    G4VisAttributes* yokeColor = new G4VisAttributes(G4Colour(0.2, 1.0, 0.2)); // Sets RGB color
    RegisterVisAtt(yokeColor); // Necessary so that TOPAS can delete the attribute if the component is rebuild during 4D behavior
    yokeLogicalVolumePointer->SetVisAttributes(yokeColor);

To create the overall physical volume for your component, use::

    fEnvelopePhys = CreatePhysicalVolume(fEnvelopeLog);

Be sure that the value on the left side of the above is exactly ``fEnvelopePhys``. This insures that TOPAS knows the overall physical volume’s name and is essential for TOPAS to support your component in 4D.

Use only the above method to create this overall physical volume. Do not use any of the methods below,
or else the rotation and translation specified in your Rot and Trans parameters will not be properly applied
(and you will see some very strange behavior, where the component suddely shifts position, just before the first run).

Additional forms of CreatePhysicalVolume allow you to place subcomponents within your component.

To place a subcomponent in the center of your logical volume lVol::

    G4VPhysicalVolume* CreatePhysicalVolume(subComponentName, G4LogicalVolume* lVol, G4VPhysicalVolume* parent);

To place a subcomponent into your logical volume lVol, with an offset or rotation::

    G4VPhysicalVolume* CreatePhysicalVolume(subComponentName, G4LogicalVolume* lVol, G4RotationMatrix* rot, G4ThreeVector* trans, G4VPhysicalVolume* parent);

To place multiple copies of the same subcomponent name into your logical volume, call::

    G4VPhysicalVolume* CreatePhysicalVolume(subComponentName, G4int copy, G4bool reuseLogical, G4LogicalVolume* lVol, G4RotationMatrix* rot, G4ThreeVector* trans, G4VPhysicalVolume* parent);

* copy should be a unique integer to differentiate the different copies of your subcomponent. This copy number is useful in some of the visualization commands when you want to control just one copy or another.
* Set reuseLogical true if you are using the same logical volume in all of these placements. This is efficient if all of the copies of the subcomponent are identical except for their placement.
* Set reuseLogical false if you are using different logical volumes in each of these placements. This allows you to make each copy of the subcomponent different (different material, different shape, different size, etc.).

To place multiple copies of the same subcomponent using a Geant4 parameterization (creating Geant4 parameterized volumes), call::

    G4VPhysicalVolume* CreatePhysicalVolume(const char* subComponentName, G4LogicalVolume* lVol, G4VPhysicalVolume* parent, const EAxis pAxis, const G4int nReplicas, G4VPVParameterisation* pParam);

To place multiple copies of the same subcomponent using a Geant4 replica volume, call::

    G4VPhysicalVolume* CreatePhysicalVolume(const char* subComponentName, G4LogicalVolume* lVol, G4VPhysicalVolume* parent, const EAxis pAxis, const G4int nReplicas, G4double width);

The last line of Construct MUST be::

    return fEnvelopePhys;

Some helper functions you may want to use from the TsParameterManager::

    G4VisAttributes* GetColor(G4String name);
    G4VisAttributes* GetColor(const char* name);
    G4VisAttributes* GetInvisible();

Some helper functions you may want to use from the TsVGeometryComponent::

    SetTooComplexForOGLS()

Call this to tell Graphics that this component has become too complex to efficiently render in OpenGL's Stored Mode. It will instead be rendered in OpenGL's Immediate Mode (can be less quick to update, but uses less memory)

::

    GetMaterial

By default, the logical volumes you create will get their material from the material parameter you specified for this component. But you can use GetMaterial to obtain any other named material.
