Optical Physics
---------------

Optical Photons
~~~~~~~~~~~~~~~

A full description of the tracking of optical photons is available in the `Geant4 Physics Reference Manual <http://geant4.cern.ch/G4UsersDocuments/UsersGuides/PhysicsReferenceManual/html/node66.html>`_ and the `Geant4 Guide for Applications Developers <http://geant4.cern.ch/G4UsersDocuments/UsersGuides/ForApplicationDeveloper/html/TrackingAndPhysics/physicsProcess.html#5.2.5>`_.

TOPAS allows to include optical physics by means of the ``g4optical`` module in the physics list. The available optical processes included in the ``g4optical`` module are: scintillation, Cerenkov radiation, wavelength shifting, optical absorption, Rayleigh scattering and boundary processes. However, this module is not sufficient to set up the generation and tracking of optical photons. The optical properties of the material of the volumes must to be defined too (at the least the refractive index must to be defined). There exist two types of variables to define the optical properties: a vector based and constant based. The vector-based parameter allows to define a property (refractive index for example) as a function of the photon’s energy. While the constant-based parameters allows to define an scalar (scintillation yield for example).

To activate the optical properties in a material one must to set::

    b:Ma/MyMaterial/EnableOpticalProperties = "True"

To set a property based on a vector, one must to define the energy of reference. For example to include the refractive index one must to define two parameters::

    dv:Ma/MyMaterial/RefractiveIndex/Energies = 3 2.0 2.5 3.0 eV
    uv:Ma/MyMaterial/RefractiveIndex/Values = 3 1.58 1.58 1.58

To set a property based on a scalar only one parameter is needed, for example::

    u:Ma/MyMaterial/ScintillationYield = 1120 # in ph/MeV
    d:Ma/MyMaterial/FastTimeConstant = 2.1 ns

The full list of parameters available is listed in the next table.

==============  ===================
Type            Parameter name
==============  ===================
uv              RefractiveIndex
uv              ImaginaryRefractiveIndex
uv              RealRefractiveIndex
dv              AbsLength
uv              FastComponent
uv              SlowComponent
uv              Miehg
uv              SpecularLobeConstant
uv              SpecularSpikeConstant
uv              BackScatterConstant
uv              WLSAbsLength
uv              WLSComponent
uv              Reflectivity
uv              Efficiency
uv              Transmittance
u               ScintillationYield ( in photons/MeV)
u               ResolutionScale
d               FastTimeConstant
d               SlowTimeConstant
u               YieldRatio
u               MiehgForward
u               MiehgBackward
u               MiehgForwardRatio
u               WLSTimeConstant
u               BirksConstant (in mm/MeV)
==============  ===================



Optical Surfaces
~~~~~~~~~~~~~~~~

If a perfect smooth interface is between two dielectric materials, the user only needs to provide the refractive index. In all other cases, a surface or optical boundary needs to be defined. There exist two kinds of surfaces: the border surface that delimits the boundary between two components; and the skin surface which surrounds one single component.
Border surface is ordered in the sense that the order of the components matters, two border surfaces can exists between a pair of components. Thus, the follow parameters define two surfaces for a pair of components::

    s:Ge/MyComponent1/OpticalBehaviorTo/MyComponent2 = "MySurface1"
    s:Ge/MyComponent2/OpticalBehaviorTo/MyComponent1 = "MySurface2"

For skin surface only one surface can be defined per component::

    s:Ge/MyComponent1/OpticalBehavior = "MySurface1"

Surfaces can be defined as follows (see next table for description)::

    s:Su/MySurfaceName/Type = "dielectric_dielectric" # or dielectric_metal

Next, choose the model for optical surfaces::

    s:Su/MySurfaceName/Model = "Glisur " # Or Unified

Finally the finish::

    s:Su/MySurfaceName/Finish = "Polished"

In addition, more detailed properties can be added by parameters described in the table below. In such a case, the way to define would be for example (with prefix ``Su`` instead of ``Ma``)::

    dv:Su/MySurfaceName/Energies = 2 1.0 4.0 eV
    uv:Su/MySurfaceName/Reflectivity = 2 0.8 0.8

========  ==============  ===============================================================
Type      Parameter name  Possible values
========  ==============  ===============================================================
string    Type            | dielectric_dielectric
                          | dielectric_metal
string    Finish          | polished: *smooth perfectly polished surface*
                          | polishedfrontpainted: *smooth top-layer (front) paint*
                          | polishedbackpainted: *same as polished but with a back-paint*
                          | ground: *rough surface*
                          | groundfrontpainted: *rough top-layer (front) paint*
                          | groundbackpainted: *same as ground but with a back-paint*
string    Model           | Unified: `reference <http://dx.doi.org/10.1109/NSSMIC.1996.591410>`_
                          | Glisur: original GEANT3.21 model
unitless  SigmaAlpha      Between 0 and 1. By default 0
========  ==============  ===============================================================
