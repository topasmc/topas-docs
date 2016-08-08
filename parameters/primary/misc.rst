Miscellaneous
-------------

Additional Control of Number of Histories
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Because TOPAS supports both sequential and random time, there are additional parameters that can control the number of histories in random mode. Read the last section of this document, TOPAS Overall Control, before using these parameters::

    i:So/Demo/NumberOfHistoriesInRandomJob = 100
    d:So/Demo/ProbabilityOfUsingAGivenRandomTime = 1.



Filtering Sources
~~~~~~~~~~~~~~~~~

Optionally filter what comes from the source. This is mainly intended for use with saved PhaseSpace, but is applied uniformly to all sources. Syntax is identical to that used for filtering in Scorers.

You may write your own additional filters (see Extending TOPAS at the end of this user guide).

Filter by Charge. Accepts one or more of "Positive", "Negative" or "Neutral"::

    sv:So/MySource/OnlyIncludeParticlesCharged = 1 "Negative"
    sv:So/MySource/OnlyIncludeParticlesNotCharged = 1 "Negative"

Filter by Atomic Mass or Number::

    i:So/MySource/OnlyIncludeParticlesOfAtomicMass = 10 # allow all ions of atomic mass 10
    i:So/MySource/OnlyIncludeParticlesNotOfAtomicMass = 10
    i:So/MySource/OnlyIncludeParticlesOfAtomicNumber = 6 # allow all ions of Carbon
    i:So/MySource/OnlyIncludeParticlesNotOfAtomicNumber = 6

Filter by Particle’s Initial Kinetic Energy::

    d:So/MySource/OnlyIncludeParticlesWithInitialKEBelow = 1. MeV
    d:So/MySource/OnlyIncludeParticlesWithInitialKENotBelow = 1. MeV
    d:So/MySource/OnlyIncludeParticlesWithInitialKE = 1. MeV
    d:So/MySource/OnlyIncludeParticlesWithInitialKENot = 1. MeV
    d:So/MySource/OnlyIncludeParticlesWithInitialKEAbove = 10. MeV
    d:So/MySource/OnlyIncludeParticlesWithInitialKENotAbove = 10. MeV

Filter by Particle’s Initial Momentum::

    d:So/MySource/OnlyIncludeParticlesWithInitialMomentumBelow = 1. MeV
    d:So/MySource/OnlyIncludeParticlesWithInitialMomentumNotBelow = 1. MeV
    d:So/MySource/OnlyIncludeParticlesWithInitialMomentum = 1. MeV
    d:So/MySource/OnlyIncludeParticlesWithInitialMomentumNot = 1. MeV
    d:So/MySource/OnlyIncludeParticlesWithInitialMomentumAbove = 10. MeV
    d:So/MySource/OnlyIncludeParticlesWithInitialMomentumNotAbove = 10. MeV

Filter by Particle Name::

    sv:So/MySource/OnlyIncludeParticlesNamed = 2 "proton" "neutron"
    sv:So/MySource/OnlyIncludeParticlesNotNamed = 2 "proton" "neutron"

Particle names are as described :ref:`here <primary_particle_names>`.

You may specify more than one filter. For example, to score protons with initial KE over 100 MeV::

    sv:So/MySource/OnlyIncludeParticlesNamed = 1 "proton"
    d:So/MySource/OnlyIncludeParticlesWithInitialKEAbove = 100. MeV # minimum energy

You can invert the results of all previous filters. The following would score only particles that are Not protons with initial KE over 100 MeV::

    sv:So/MySource/OnlyIncludeParticlesNamed = 2 "proton" "neutron"
    d:So/MySource/OnlyIncludeParticlesWithInitialKEAbove = 100. MeV # minimum energy
    b:So/MySource/InvertFilter = "True"

Any filter property can be set by time features if you wish, to produce time-dependent filtering.
