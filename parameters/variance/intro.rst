Introduction
------------

Please note that Variance Reduction is highly dependent on your specific geometry. Approach these features with caution and test all variance reduced setups against an equivalent setup without variance reduction.

You should also review the Geant4 document that describes which cases are problematic `here <https://geant4.web.cern.ch/geant4/collaboration/working_groups/geometry/biasing/BiasScoreUseCases.html>`_.

To enable the particle split applied to protons::

    b:Vr/UseVarianceReduction = "true"
    b:Vr/ParticleSplit/Active = "true"
    sv:Vr/ParticleSplit/ParticleName = 1 "proton"



To Specify the Split Geometry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The geometry for variance reduction must to be a parallel one. The type of component can be any standard solid (generic solid) defined in the geometry section. The geometry must to consists of a geometrical component with a set of geometrical sub-components as daughters. The sub- components must to be located in such a way that the borders in between coincide. The split process or Russian roulette will occur at that borders. In the next figure a simple scheme is shown.

.. image:: split_geometry.png

Time features can be used to move or rotate the component or sub-components. But there is a restriction: the implementation of VRT does not allow to change the dimensions of the component and sub-components.

To set the geometry for VRT::

    s:Vr/ParticleSplit/Component = "MyComponent"
    sv:Vr/ParticleSplit/SubComponents = n "MySubComp_1" ... "MySubComp_n"



To Define the Splitting Technique
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There is three variance reduction techniques available: GeometricalParticleSplit, ImportanceSampling and WeightWindow
To chose a technique, use for example::

    s:Vr/ParticleSplit/Type = "GeometricalParticleSplit"
