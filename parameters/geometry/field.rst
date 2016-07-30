Electromagnetic Fields
----------------------

You can assign an electric, magnetic or combined electromagnetic field to any geometry component (with exception of Group components). The field will extend into any child components unless they themselves have their own field.

To assign a field, add the parameter "Field", as in::

    s:Ge/MyComponent/Field = "DipoleMagnet" # "DipoleMagnet", "QuadrupoleMagnet", "MappedMagnet", "UniformElectroMagnetic" or your own definition

For "DipoleMagnet", specify dipole field and strength, as in (see :ref:`example_special_dipole`)::

    u:Ge/MyComponent/MagneticFieldDirectionX = 0.0
    u:Ge/MyComponent/MagneticFieldDirectionY = 1.0
    u:Ge/MyComponent/MagneticFieldDirectionZ = 0.0
    d:Ge/MyComponent/MagneticFieldStrength = 3.0 tesla

For "QuadrupoleMagnet", specify the two components of the gradient, as in (see :ref:`example_special_quadrupole`)::

    d:Ge/MyComponent/MagneticFieldGradientX = 1.0 tesla
    d:Ge/MyComponent/MagneticFieldGradientY = 1.0 tesla

For "MappedMagnet", specify a field map in the Opera 3D format, as in (see :ref:`example_special_purgingmagnet`)::

    s:Ge/MyComponent/MagneticField3DTable = "PurgMag3D.TABLE"

For "UniformElectroMagnetic", specify electric field and dipole magnetic field, as in (see :ref:`example_special_electromagnet`)::

    u:Ge/MyComponent/ElectricFieldDirectionX = 1.0
    u:Ge/MyComponent/ElectricFieldDirectionY = 1.0
    u:Ge/MyComponent/ElectricFieldDirectionZ = 0.0
    d:Ge/MyComponent/ElectricFieldStrength   = 5000 kV/cm
    u:Ge/MyComponent/MagneticFieldDirectionX = 0.0
    u:Ge/MyComponent/MagneticFieldDirectionY = 1.0
    u:Ge/MyComponent/MagneticFieldDirectionZ = 0.0
    d:Ge/MyComponent/MagneticFieldStrength   = 5.0 tesla

If you have any other value in Field, TOPAS will look in your extensions to find your own class that defines this field. See the Extensions section at the end of this User Guide for more details.

Field orientation is set by rotating the component.

As with almost any TOPAS parameter, the Electric Field Strength, Dipole Magnet Strength, Quadrupole Magnet Gradient or Mapped Magnetic Field file can be set to change over time by using Time Features such as (see :ref:`example_special_quadanddipole`)::

    d:Ge/MyComponent/MagneticFieldStrength = Tf/BField1st/Value tesla

Fine control of the stepping algorithm can be done by changing the following parameters from their default values::

    s:Ge/MyComponent/FieldStepper = "ClassicalRK4"
    d:Ge/MyComponent/FieldStepMinimum = 1.0 mm
    d:Ge/MyComponent/FieldDeltaChord = 1.0e-1 mm

See the `Geant4 Application Developers Guide <https://geant4.web.cern.ch/geant4/UserDocumentation/UsersGuides/ForApplicationDeveloper/html/ch04s03.html>`_ for detailed discussion of these options.

Stepper choices for purely magnetic fields are: "ExplicitEuler", "ImplicitEuler", "SimpleRunge", "SimpleHeum", "HelixExplicitEuler", "HelixImplicitEuler", "HelixSimpleRunge", "CashKarpRKF45", "RKG3" and "ClassicalRK4".

Stepper choices for electroMagnetic fields are: "ExplicitEuler", "ImplicitEuler", "SimpleRunge", "SimpleHeum" and "ClassicalRK4".
