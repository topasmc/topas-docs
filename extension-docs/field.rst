.. _extension_fields:

Custom Fields
=============

.. highlight:: c++

While an ElectroMagnetic Field can have just an electric field, just a magnetic field, or a combination of the two, Geant4's architecture does not provide any base class for a purely electric field, but instead provides one base class for purely Magnetic fields and another for combined ElectroMagnetic fields. To allow you to use all features of both Geant4 classes, TOPAS emulates this curious aspect of Geant4's design.

If you want to create a purely magnetic field, the first line of the cc file should be of the form::

    // Magnetic Field for MyField1

If you want to create a purely electric field, or a combined electromagnetic field, the first line of the cc file should be of the form::

    // ElectroMagnetic Field for MyField1

and then if what you really wanted was just an electric field, you implement the magnetic field strength as just zero.

Geant4 will call your GetFieldValue every time it needs to query the field. For reasons that are not clear to this author, Geant4 will sometimes query your field for points outside of your intended geometry component, so make sure to return at least some value (at least a zero) for every possible point.

Parameter lookups should be done in ResolveParameters. Call ResolveParameters directly from your constructor, and then you can also rely on TOPAS to re-call this method any time one of this field class's parameters is changed.
