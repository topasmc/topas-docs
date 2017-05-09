.. _extension_physics:

Custom Physics Lists and Physics Modules
========================================

.. highlight:: c++

First line of the cc file must be of the form::

    // Physics List for MyPhysicsList1
    or
    // Physics Module for MyPhysicsModule1

You can supply your own physics list or physics module. Note however that this option is not recommended unless you have significant Geant4 expertise. Even most long-time Geant4 users get into difficultly writing their own physics lists and physics modules. Wherever possible, you should try to use one of the Reference physics list or the Modular physics list with pre-written Geant4 physics modules.

The example physics list and physics module provided in topas/extensions/MyPhysicsList1 and MyPhysicsModule include pointers to the TOPAS parameter manager as their arguments. This is not required, but allows you to use TOPAS parameters to adjust options within your list or modules.
