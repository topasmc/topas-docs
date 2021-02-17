Secondary Biasing
-----------------

The split of secondary particles created after an electromagnetic interaction is also supported. A common example is the split of secondary photons created in the bremsstrahlung process for conventional radiotherapy simulations.

This variance reduction works per electromagnetic physical process per region. :ref:`physics_regions` allow multiple components to have specific production cuts. This is useful in complex geometry setups to improve the computational speed by assigning high production cuts in regions where detailed simulation is unimportant. To assign a region to a component::

    s:Ge/MyComponent/AssignToRegionNamed = "MyRegion"

The region ``MyRegion`` is automatically created if it does not exist. The next step is to set the secondary biasing option::

    s:Vr/ParticleSplit/Type = "SecondaryBiasing"

Then three vectors must be defined. One with the name of the electromagnetic processes, one with the split number for each process and one with the maximum energies for each processes. The biased particles with energies larger than these values are subject to Russian roulette::

    sv:Vr/ParticleSplit/ForRegion/MyRegion/ProcessesNamed = 2 "eBrem" "compt"
    uv:Vr/ParticleSplit/ForRegion/MyRegion/SplitNumber = 2 100 10
    dv:Vr/ParticleSplit/ForRegion/MyRegion/MaximumEnergy = 2 6.0 0.511 MeV

If suitable, further CPU time can be saved with a directional Russian roulette for secondary particles created with split (analogous to :ref:`vr_geometrical_splitting`). For that, a new VRT must be set:: 

    s:Vr/DirectionalFilter/Type = "DirectionalRussianRoulette"
    
Later, a reference component must to be chosen::

    s:Vr/DirectionalFilter/ReferenceComponent = "Target"

And the directional filter is applied::

    dv:Vr/DirectionalFilter/ForRegion/MyRegion/DirectionalSplitLimits = 2 1.0 1.0 m
    dv:Vr/DirectionalFilter/ForRegion/MyRegion/DirectionalSplitRadius = 2 5.0 5.0 cm
    sv:vr/DirectionalFilter/ForRegion/MyRegion/processesNamed = 2 "eBrem" "compt"

.. image:: secondary_biasing.png

Figure: Biasing particle of secondary photons after a bremsstrahlung process. On the left, no directional Russian roulette is applied. On the right, a directional Russian roulette is applied.
