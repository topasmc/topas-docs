Weight Window
-------------

In this technique, the split process or Russian roulette will be applied depending on the statistical weight of the particle. Every time that a particle crosses from a sub-component to the next one, the statistical weight is evaluated. Particles with statistical weights larger than a lower weight bound and lower than a upper weight bound will be tracked normally. Particles with statistical weights lower than a lower weight bound will be subject to Russian roulette. If survives the particle is tracking normally but its statistical weight is increased. Particles with statistical weights larger than an upper weight bound will be split, and low statistical weights are assigned to the new particles. The split number and Russian roulette criteria are internally calculated from a energy map, a weight map, a upper limit factor and a survival factor. In simple geometries the maps can be input by hand.

The user must to provide a double vector with upper energy bounds and an unitless vector with lower weight bounds for every sub-component: WeightMap and EnergyMap. The inverse of a value named MaximumSplitNumber (100 as default) is used to specify the minimum survival probability to be used in Russian roulette. The parameter PlaceOfAction states if the split process (or Russian roulette) will occurs at the boundary of the sub-components, at physics interaction or at both.

The follow configuration is equivalent to importance sampling with importance generator of 2::

    s:Vr/ParticleSplit/Type = "WeightWindow"
    uv:Vr/ParticleSplit/WeightMap = 4 1. 1. 0.125 0.0615
    dv:Vr/ParticleSplit/EnergyMap = 4 1. 1. 1. 1. GeV
    u:Vr/ParticleSplit/UpperLimitFactor = 1
    u:Vr/ParticleSplit/SurvivalFactor = 1
    i:Vr/ParticleSplit/MaximumSplitNumber = 100
    s:Vr/ParticleSplit/PlaceOfAction = "onBoundary"
    #Others options of PlaceOfAction: "OnCollision" and "OnBoundaryAndCollision"

.. image:: weight_window.png
