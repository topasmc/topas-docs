Custom Physics Lists
====================

.. highlight:: c++

First line of the cc file must be of the form::

    // Physics List for MyPhysicsList1

You can supply your own physics list. Note however that this option is not recommended unless you have significant Geant4 expertise. Even most long-time Geant4 users get into difficultly writing their own physics lists. Wherever possible, you should try to use one of the Reference physics list or the Modular physics list.

The example physics list provided in topas/extensions/TsPhysicsList1 includes a pointer to the TOPAS parameter manager as its argument. This is not required, but allows you to use TOPAS parameters to adjust options within your physics list.
