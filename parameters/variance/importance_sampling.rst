.. _vr_importance_sampling:

Importance Sampling
-------------------

In this technique, an importance value is assigned to each sub-component. If a particle is transported into a sub-component with a higher importance, then the particle is split. If it is transported into a sub-component with a lower importance, then Russian roulette is played. By default an importance value of 1 is automatically assigned to the parent component and to the world.

.. warning::

    It is desirable for the thickness of the sub-components to be similar to the mean free path of the physical process to be biased.

The sub-component importance values are defined by hand. For example, to split the particles by a factor of 2 between subsequent sub-components, one must to define::

    s:Vr/ParticleSplit/Type = "ImportanceSampling"
    uv:Vr/ParticleSplit/ImportanceValues = 5 1 2 4 8 16

.. image:: importance_sampling.png
