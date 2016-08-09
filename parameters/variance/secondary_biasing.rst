Secondary Biasing
-----------------

The split of secondary particles created after an electromagnetic interaction is also supported. A common example is the split of secondary photons created in bremsstrahlung process for conventional radiotherapy simulations. This variance reduction works per electromagnetic physical process per region. A region allows to multiple components to have specific production cuts. This is useful in complex geometry setups to improve the computational speed by assigning high production cuts in regions where detailed simulation is not important. To assign a region to a component, user can proceed as follows::

    s:Ge/MyComponent/AssignToRegionNamed = "MyRegion"

The region MyRegion is automatically created if it not exists. The next step is to set secondary biasing option::

    s:Vr/ParticleSplit/Type = "SecondaryBiasing"

After that three vectors must to be defined. One with the name of the electromagnetic processes, one with the split number for each process and one with the maximum energies for each processes. The biased particles with energies larger than this values are subject to Russian roulette::

    sv:Vr/ParticleSplit/ForRegion/MyRegion/ProcessesNamed = 2 "eBrem" "compt"
    uv:Vr/ParticleSplit/ForRegion/MyRegion/SplitNumber = 2 100 10
    dv:Vr/ParticleSplit/ForRegion/MyRegion/MaximumEnergy = 2 6.0 0.511 MeV

If suitable, further CPU time can be saved with a directional Russian roulette for secondary particles created with split (analogous to Geometrical particle split). For that, a reference component must to be chosen::

    s:Vr/ParticleSplit/ReferenceComponent = "Target"

And the directional filter is applied::

    dv:Vr/ParticleSplit/ForRegion/MyRegion/DirectionalSplitLimits = 2 1.0 1.0 m
    dv:Vr/ParticleSplit/ForRegion/MyRegion/DirectionalSplitRadius = 2 5.0 5.0 cm

.. image:: secondary_biasing.png

Figure: Biasing particle of secondary photons after a bremsstrahlung process. On the left no directional Russian roulette, on the right a directional Russian roulette is applied.
