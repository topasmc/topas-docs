.. _scoring_filter:

Filtering Scorers
-----------------

You may add filters to limit what is scored.

You may assign more than one filter to the same scorer.
When you have more than one filter, they work as an "AND".

You may write your own additional filters (see :ref:`extension_filter`).

Filter by Generation. Accepts either ``"Primary"`` or ``"Secondary"``::

    s:Sc/MyScorer/OnlyIncludeParticlesOfGeneration = "Primary"

Filter by Charge. Accepts one or more of ``"Positive"``, ``"Negative"`` or ``"Neutral"``::

    sv:Sc/MyScorer/OnlyIncludeParticlesCharged = 1 "Negative"
    sv:Sc/MyScorer/OnlyIncludeParticlesNotCharged = 1 "Negative"

Filter by Atomic Mass or Number::

    i:Sc/MyScorer/OnlyIncludeParticlesOfAtomicMass = 10    # allow all ions of atomic mass 10
    i:Sc/MyScorer/OnlyIncludeParticlesNotOfAtomicMass = 10
    i:Sc/MyScorer/OnlyIncludeParticlesOfAtomicNumber = 6   # allow all ions of Carbon
    i:Sc/MyScorer/OnlyIncludeParticlesNotOfAtomicNumber = 6

Filter by Particle’s Initial Kinetic Energy::

    d:Sc/MyScorer/OnlyIncludeParticlesWithInitialKEBelow = 1. MeV
    d:Sc/MyScorer/OnlyIncludeParticlesWithInitialKENotBelow = 1. MeV
    d:Sc/MyScorer/OnlyIncludeParticlesWithInitialKE = 1. MeV
    d:Sc/MyScorer/OnlyIncludeParticlesWithInitialKENot = 1. MeV
    d:Sc/MyScorer/OnlyIncludeParticlesWithInitialKEAbove = 10. MeV
    d:Sc/MyScorer/OnlyIncludeParticlesWithInitialKENotAbove = 10. MeV

When designing energy or momentum filters, keep in mind that since no vacuum is perfect in Geant4 (density can be low but cannot be exactly zero), even particles traveling through ``"Vacuum"`` will experience some energy loss.

Filter by Particle’s Initial Momentum::

    d:Sc/MyScorer/OnlyIncludeParticlesWithInitialMomentumBelow = 1. MeV
    d:Sc/MyScorer/OnlyIncludeParticlesWithInitialMomentumNotBelow = 1. MeV
    d:Sc/MyScorer/OnlyIncludeParticlesWithInitialMomentum = 1. MeV
    d:Sc/MyScorer/OnlyIncludeParticlesWithInitialMomentumNot = 1. MeV
    d:Sc/MyScorer/OnlyIncludeParticlesWithInitialMomentumAbove = 10. MeV
    d:Sc/MyScorer/OnlyIncludeParticlesWithInitialMomentumNotAbove = 10. MeV

Filter by Kinetic Energy of Particle or its Ancestor when it hit the Scoring Component (excludes any particles descended from primaries that originated in the component)::

    d:Sc/MyScorer/OnlyIncludeIfIncidentParticleKEBelow = 1. MeV
    d:Sc/MyScorer/OnlyIncludeIfIncidentParticleKENotBelow = 1. MeV
    d:Sc/MyScorer/OnlyIncludeIfIncidentParticleKE = 1. MeV
    d:Sc/MyScorer/OnlyIncludeIfIncidentParticleKENot = 1. MeV
    d:Sc/MyScorer/OnlyIncludeIfIncidentParticleKEAbove = 10. MeV
    d:Sc/MyScorer/OnlyIncludeIfIncidentParticleKENotAbove = 10. MeV

Filter by Initial Momentum of Particle or its Ancestor when it hit the Scoring Component (excludes any particles descended from primaries that originated in the component)::

    d:Sc/MyScorer/OnlyIncludeIfIncidentParticleMomentumBelow = 1. MeV
    d:Sc/MyScorer/OnlyIncludeIfIncidentParticleMomentumNotBelow = 1. MeV
    d:Sc/MyScorer/OnlyIncludeIfIncidentParticleMomentum = 1. MeV
    d:Sc/MyScorer/OnlyIncludeIfIncidentParticleMomentumNot = 1. MeV
    d:Sc/MyScorer/OnlyIncludeIfIncidentParticleMomentumAbove = 10. MeV
    d:Sc/MyScorer/OnlyIncludeIfIncidentParticleMomentumNotAbove = 10. MeV

Filter by Process that created the particle. Allows one or more process name::

    sv:Sc/MyScorer/OnlyIncludeParticlesFromProcess = 2 "hIoni" "eBrem"
    sv:Sc/MyScorer/OnlyIncludeParticlesNotFromProcess = 2 "hIoni" "eBrem"

Filter by Process that created the particle or any of its ancestors::

    sv:Sc/MyScorer/OnlyIncludeIfParticleOrAncestorFromProcess = 2 "hIoni" "eBrem"
    sv:Sc/MyScorer/OnlyIncludeIfParticleOrAncestorNotFromProcess = 2 "hIoni" "eBrem"

Filter by Particle Name::

    sv:Sc/MyScorer/OnlyIncludeParticlesNamed = 2 "proton" "neutron"
    sv:Sc/MyScorer/OnlyIncludeParticlesNotNamed = 2 "proton" "neutron"

Filter by Particle Name or the name of any of the particle’s ancestors. Use this to, for example, score all charge that results from neutrons, even if the final particle is not a neutron::

    sv:Sc/MyScorer/OnlyIncludeIfParticleOrAncestorNamed = 1 "neutron"
    sv:Sc/MyScorer/OnlyIncludeIfParticleOrAncestorNotNamed = 1 "neutron"

Particle names are as described :ref:`here <particle_names>`.

Filter by Particle’s Origin Volume, Component, or Component and Subcomponents::

    sv:Sc/MyScorer/OnlyIncludeParticlesFromVolume = 1 "Propeller20/Leaf"
    sv:Sc/MyScorer/OnlyIncludeParticlesNotFromVolume = 1 "Propeller20/Leaf"
    sv:Sc/MyScorer/OnlyIncludeParticlesFromComponent = 1 "Jaws"
    sv:Sc/MyScorer/OnlyIncludeParticlesNotFromComponent = 1 "Jaws"
    sv:Sc/MyScorer/OnlyIncludeParticlesFromComponentOrSubComponentsOf = 1 "Nozzle"
    sv:Sc/MyScorer/OnlyIncludeParticlesNotFromComponentOrSubComponentsOf = 1 "Nozzle"

If you specify multiple Volume or Component names, this is interpreted as an "OR", not "AND".

You will see that you can specify a single Volume or a Component.

    sv:Sc/OnlyIncludeParticlesFromVolume/OnlyIncludeParticlesFromVolume = 2 "World" "Foil"    sv:Sc/OnlyIncludeParticlesFromComponent/OnlyIncludeParticlesFromComponent = 2 "World" "Foil"If the Component is a simple one, like a box or a sphere, then the component only has a single G4Volume, so the two are functionally identical.But if the Component is a more complicated one, like a Range Modulator Wheel, then there are multiple G4Volumes in the Component, and the latter would allow one to do things like tell just which particles interacted in the Wheel's "stop block". 


Filter by Particle or its Ancestor’s Origin Volume, Component, or Component and Subcomponents::

    sv:Sc/MyScorer/OnlyIncludeIfParticleOrAncestorFromVolume = 1 "Propeller20/Leaf"
    sv:Sc/MyScorer/OnlyIncludeIfParticleOrAncestorNotFromVolume = 1 "Propeller20/Leaf"
    sv:Sc/MyScorer/OnlyIncludeIfParticleOrAncestorFromComponent = 1 "Jaws"
    sv:Sc/MyScorer/OnlyIncludeIfParticleOrAncestorNotFromComponent = 1 "Jaws"
    sv:Sc/MyScorer/OnlyIncludeIfParticleOrAncestorFromComponentOrSubComponentsOf = 1 "Nozzle"
    sv:Sc/MyScorer/OnlyIncludeIfParticleOrAncestorNotFromComponentOrSubComponentsOf = 1 "Nozzle"

Filter by whether Particle Interacted in Volume, Component, or Component and Subcomponents::

    sv:Sc/MyScorer/OnlyIncludeIfParticleInteractedInVolume = 1 "Propeller20/Leaf"
    sv:Sc/MyScorer/OnlyIncludeIfParticleNotInteractedInVolume = 1 "Propeller20/Leaf"
    sv:Sc/MyScorer/OnlyIncludeIfParticleInteractedInComponent = 1 "Jaws"
    sv:Sc/MyScorer/OnlyIncludeIfParticleNotInteractedInComponent = 1 "Jaws"
    sv:Sc/MyScorer/OnlyIncludeIfParticleInteractedInComponentOrSubComponentsOf = 1 "Nozzle"
    sv:Sc/MyScorer/OnlyIncludeIfParticleNotInteractedInComponentOrSubComponentsOf = 1 "Nozzle"

Filter by Particle or its Ancestor Interacted in Volume, Component, or Component and Subcomponents::

    sv:Sc/MyScorer/OnlyIncludeIfParticleOrAncestorInteractedInVolume = 1 "Propeller20/Leaf"
    sv:Sc/MyScorer/OnlyIncludeIfParticleOrAncestorNotInteractedInVolume = 1 "Propeller20/Leaf"
    sv:Sc/MyScorer/OnlyIncludeIfParticleOrAncestorInteractedInComponent = 1 "Jaws"
    sv:Sc/MyScorer/OnlyIncludeIfParticleOrAncestorNotInteractedInComponent = 1 "Jaws"
    sv:Sc/MyScorer/OnlyIncludeIfParticleOrAncestorInteractedInComponentOrSubComponentsOf = 1 "Nozzle"
    sv:Sc/MyScorer/OnlyIncludeIfParticleOrAncestorNotInteractedInComponentOrSubComponentsOf = 1 "Nozzle"

Filter by whether Particle Traversed Volume, Component, or Component and Subcomponents::

    sv:Sc/MyScorer/OnlyIncludeIfParticleTraversedVolume = 1 "Propeller20/Leaf"
    sv:Sc/MyScorer/OnlyIncludeIfParticleNotTraversedVolume = 1 "Propeller20/Leaf"
    sv:Sc/MyScorer/OnlyIncludeIfParticleTraversedComponent = 1 "Jaws"
    sv:Sc/MyScorer/OnlyIncludeIfParticleNotTraversedComponent = 1 "Jaws"
    sv:Sc/MyScorer/OnlyIncludeIfParticleTraversedComponentOrSubComponentsOf = 1 "Nozzle"
    sv:Sc/MyScorer/OnlyIncludeIfParticleNotTraversedComponentOrSubComponentsOf = 1 "Nozzle"

Filter by Particle or its Ancestor Traversed Volume, Component, or Component and Subcomponents::

    sv:Sc/MyScorer/OnlyIncludeIfParticleOrAncestorTraversedVolume = 1 "Propeller20/Leaf"
    sv:Sc/MyScorer/OnlyIncludeIfParticleOrAncestorNotTraversedVolume = 1 "Propeller20/Leaf"
    sv:Sc/MyScorer/OnlyIncludeIfParticleOrAncestorTraversedComponent = 1 "Jaws"
    sv:Sc/MyScorer/OnlyIncludeIfParticleOrAncestorNotTraversedComponent = 1 "Jaws"
    sv:Sc/MyScorer/OnlyIncludeIfParticleOrAncestorTraversedComponentOrSubComponentsOf = 1 "Nozzle"
    sv:Sc/MyScorer/OnlyIncludeIfParticleOrAncestorNotTraversedComponentOrSubComponentsOf = 1 "Nozzle"

Filter by material::

    sv:Sc/MyScorer/OnlyIncludeIfInMaterial = 2 "G4_WATER" "Air"
    sv:Sc/MyScorer/OnlyIncludeIfNotInMaterial = 2 "G4_WATER" "Air"

Note that in this case, the material name must exactly match the case defined in Geant4.  To check what materials have been defined, add the parameter::

    i:Ma/Verbosity = 1

Filter on DICOM RT Structure Sets:
A structure set is an extra file in the DICOM directory that provides information on structures such as organs, tumors, PTVs, etc. that have been outlined (contoured) in the planing process. The data is stored as a set of polygons, up to one per slice for each contoured structure. TOPAS can color code DICOM components according to this structure information (see :ref:`geometry_patient_dicom`) and can filter scoring based on these structures::

    sv:Sc/MyScorer/OnlyIncludeIfInRTStructure = 2 "R_LUNG" "L_LUNG"

If the structure name includes a space, substitute an underscore in the parameter. So, for example, if the structure name is "R LUNG", you should supply the parameter as "R_LUNG".

The scored value is set to -1 if the given voxel is not in one of the named structures.

For Surface Scorers, you can also filter by whether particle is going ``"In"`` or ``"Out"`` of scoring surface. Omit this filter to allow either option::

    s:Sc/MyScorer/OnlyIncludeParticlesGoing = "In"

You may specify more than one filter. For example, to score protons with initial KE over 100 MeV::

    sv:Sc/MyScorer/OnlyIncludeParticlesNamed = 1 "proton"
    d:Sc/MyScorer/OnlyIncludeParticlesWithInitialKEAbove = 100. MeV # minimum energy

You can invert the results of all previous filters. The following would score only particles that are Not protons with initial KE over 100 MeV::

    sv:Sc/MyScorer/OnlyIncludeParticlesNamed = 2 "proton" "neutron"
    d:Sc/MyScorer/OnlyIncludeParticlesWithInitialKEAbove = 100. MeV # minimum energy
    b:Sc/MyScorer/InvertFilter = "True"

Any filter property can be set by :ref:`time_feature` if you wish, to produce time-dependent filtering.
