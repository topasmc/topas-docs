.. _vr_secondary_biasing:

Secondary Biasing
=================

The split of secondary particles created after an electromagnetic interaction is also supported. A common example is the split of secondary photons created in the bremsstrahlung process for conventional radiotherapy simulations.

This variance reduction works per electromagnetic physical process per region. :ref:`physics_regions` allow multiple components to have specific production cuts. This is useful in complex geometry setups to improve the computational speed by assigning high production cuts in regions where detailed simulation is unimportant. To assign a region to a component::

    s:Ge/MyComponent/AssignToRegionNamed = "MyRegion"

The region ``MyRegion`` is automatically created if it does not exist. The next step is to set the secondary biasing option::

    s:Vr/ParticleSplit/Type = "SecondaryBiasing"

Then three vectors must be defined. One with the name of the electromagnetic processes, one with the split number for each process and one with the maximum energies for each processes. Particles with energy less than this are split according to SplitNumber and their statistical weight reduced by a factor of SplitNumber. Particles with energies larger than these values are subject to Russian roulette::

    sv:Vr/ParticleSplit/ForRegion/MyRegion/ProcessesNamed = 2 "eBrem" "compt"
    uv:Vr/ParticleSplit/ForRegion/MyRegion/SplitNumber = 2 100 10
    dv:Vr/ParticleSplit/ForRegion/MyRegion/MaximumEnergy = 2 6.0 0.511 MeV

If suitable, further CPU time can be saved with a directional Russian roulette for secondary particles created::

    b:Vr/ParticleSplit/UseDirectionalSplitting = "True"
    d:Vr/ParticleSplit/TransX = 0.0 mm
    d:Vr/ParticleSplit/TransY = 0.0 mm
    d:Vr/ParticleSplit/TransZ = 0.0 mm
    d:Vr/ParticleSplit/Rmax = 21 mm

This creates an ROI at the centre of the world. If the created secondaries are projected to land in this ROI, they are kept. If not, they have a 1/N chance of surviving, where N is the same as SplitNumber. Particles which do survive this roulette process have their statistical weight increased by a factor of N.
