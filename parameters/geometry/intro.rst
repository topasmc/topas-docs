.. _geometry_intro:

Introduction
------------

All Geometry Components must have at least the following parameters::

    s:Ge/MyComponent/Parent = "World"
    s:Ge/MyComponent/Type = "TsBox"
    d:Ge/MyComponent/TransX=0.0 cm # defaults to 0
    d:Ge/MyComponent/TransY=0.0 cm # defaults to 0
    d:Ge/MyComponent/TransZ=0.0 cm # defaults to 0
    d:Ge/MyComponent/RotX=0.0 deg # defaults to 0
    d:Ge/MyComponent/RotY=0.0 deg # defaults to 0
    d:Ge/MyComponent/RotZ=0.0 deg # defaults to 0

The ``Parent``, ``Trans`` and ``Rot`` parameters place a component within its "mother" as described in :ref:`geometry_placement`.

Each ``Type`` has its own set of additional required parameters, discussed elsewhere for each specific component type.

The World can be either a TsBox, TsSphere or TsCylinder.

The component name can include the forward slash character ``/``, and this is used in many examples to give some hints about component hierarchy , such as::

    s:Ge/VBox2/Dipole/Parent = "Nozzle"

This bit of hierarchy in the component name, such as ``VBox2/Dipole``, does NOT actually control how the components are assembled. The actual control is from the ``Parent`` parameter (discussed :ref:`here <geometry_placement>`). The forward slash is just another character here. You could just as well use ``VBox2_Dipole`` or ``VBox2Dipole``, as long as you use the same exact string whenever you refer to this component.

Components that are in the real world (as opposed to :ref:`geometry_parallel`) must also have a material::

    s:Ge/MyComponent/Material = "Air"

To deactivate a Component (and all its children), you can either comment out the parameter that sets its ``Parent``, or set its ``Include`` parameter to false, as in::

    b:Ge/MyComponent/Include = "False" # defaults to "True"

While it is not forbidden to have unused components (components that are never assigned a ``Parent``), this can often be a sign that you have not correctly assigned the parents in your geometry. Accordingly, we check for unused components on startup and given a warning message if any are found. You can disable this warning message by setting::

    Ge/CheckForUnusedComponents = "False"

In some cases you may want to keep unused components around. This can be like keeping extra pieces of unused laboratory equipment handy on a shelf. They will have no effect on your simulation, but remain available to quickly plug in when needed by assigning a parent and setting placement parameters.

Physics control for a specific component is done as part of the ``Ge/`` parameters for that component rather than in the ``Ph/`` parameters, such as::

    d:Ge/MyComponent/MaxStepSize = 1. mm # sets maximum step size used in this component
