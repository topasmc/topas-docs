Importance Sampling
-------------------

In this technique, an importance value is assigned to each sub-component. If a particle goes from a sub-component with an importance value lower than importance value of the sub-component in which the particle enters, then the particle is split. If the opposite happens, then Russian roulette is played. By default an importance value of 1 is automatically assigned to the component that contains the sub- components and to the world.

A thickness of the sub-components of about the mean free path of the physical process to be biased is desirable. For the implementation, the importance values are defined by hand. For example, to split the particles by a factor of 2 between subsequent sub-components, one must to define::

    s:Vr/ParticleSplit/Type = "ImportanceSampling"
    uv:Vr/ParticleSplit/ImportanceValues = 5 1 2 4 8 16

.. image:: importance_sampling.png
