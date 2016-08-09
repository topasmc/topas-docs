.. _source_intro:

Introduction
------------

We allow any number of particle sources, zero, one or many, with no limitation on how they can be mixed.

We provide four different types of particle sources, each with many options:

* Parameterized Beam
* Emittance Parameterization (formerly called Twiss)
* Isotropic
* Phase Space

And you may also write your own entirely new particle source (see Extending TOPAS at the end of this user guide).

The position of the source is always the center of an associated Geometry Component. This is in keeping with the general TOPAS paradigm that all geometrical information resides in the Components. We know that this may feel odd to experienced Geant4 users who are used to setting beam directions irrespective of any geometry volumes, but the TOPAS paradigm enables sources, components, scorers and even fields to all move together in an internally consistent manner.

The Geometry Component associated with a Particle Source is often a Group Component. Such components have a center position and orientation but no actual shape or extent. The Particle Source is placed at this center position and orientation. If the Component is some other Type, such as a TsBox or TsCylinder, the Particle Source still only takes center position and orientation from this Component. None of the other aspects of the Component, such as the Component's shape or size, have any impact on the Particle Source. So, for example, the shape and size of a Beam source is set by various BeamPosition parameters, not by the Component's shape or size.

Some examples place the source at a vacuum window at the entrance to a nozzle. The source then moves as the nozzle moves.



.. _particle_names:

Particle Names
~~~~~~~~~~~~~~

Throughout TOPAS, particle names can take the following forms (case does not matter):

* A simple string such as

    * "proton"

* A string describing an ion with arguments Z, A, and optionally Charge, such as:

    * "GenericIon(6,12,6)"
    * "GenericIon(6,12)" - Charge defaults to Z, that is, the ion is fully stripped
    * When used to filter sources, ions must be fully stripped (this is the only kind of ion that Geant4's primary particle generation supports).
    * When used to filter scoring, ions can have any Charge, and any of the arguments can have wildcard value ``*`` so, for example, "GenericIon(6,*,*)" will score any Carbon ion (any A and any Charge).

* An integer PDG code, still contained in quotation marks, such as

    * "11"
    * PDG codes are as defined by the `Particle Data Group <http://pdg.lbl.gov/2012/mcdata/mc_particle_id_contents.html>`_

* When PDG code has 10 digits and starts with 100, this is passed to Geant4 either as the appropriate Geant4 light ion name ("alpha", "deuteron", "He3" or "triton") or as GenericIon(Z,A) where:

    * Characters 4-6 give Z
    * Characters 7-9 give A
    * Character 10 gives Isomer level (not used)

The full set of known particles depends on the physics you have defined. Some common values, with associated PDG codes:

=================   =========
Particle            PDG code
=================   =========
"proton"            "2212"
"neutron"           "2112"
"e-"                "11"
"e+"                "-11"
"gamma"             "22"
"He3"               "100002003"
"alpha"             "100002004"
"deuteron"          "100001002"
"triton"            "100001003"
"opticalphoton"     "0" (PDG group has no code for this particle)
"geantino"          "0" (sees transportation processes but no physics, no PDG code)
"chargedgeantino"   "0" (same as above but with charge, no PDG code)
=================   =========



Isotropic Sources
~~~~~~~~~~~~~~~~~

Isotropic sources emit particles evenly from the center of the specified Component. Specify source
type as::

    s:So/MySource/Type = “Isotropic”

