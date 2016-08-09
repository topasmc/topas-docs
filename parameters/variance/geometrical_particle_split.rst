Geometrical Particle Splitting
------------------------------

TOPAS variance reduction is further described in: Ramos-Méndez et al, “Geometrical splitting technique to improve the computational efficiency in Monte Carlo calculations for proton therapy,” Med. Phys. 40, 041718 (2013)
This technique was designed for heavy charged particles. In this implementation, you must to specify if the beam entering into the subcomponenti has cylindrical symmetry or not, that is because the particles can be or not randomly redistributed around the SplitAxis. The Russian Roulette is applied in direction. That is, at the split plane and prior to be split, the particle is subject to Russian Roulette if its direction does not point towards a Region of Interest (ROI). Then the radius of the ROI and its position on the SplitAxis must to be defined too. Further, Russian Roulette can be turned on/off at specific surfaces between sub-components.

.. code::

    s:Vr/ParticleSplit/Type = "GeometricalParticleSplit"
    s:Vr/ParticleSplit/SplitAxis = "zaxis"
    d:Vr/ParticleSplit/RussianRoulette/ROIRadius = 7.8 cm
    d:Vr/ParticleSplit/RussianRoulette/ROITrans = 10 cm
    bv:Vr/ParticleSplit/RussianRoulette = 2 "false" "true"

To set if the region at each subcomponenti is symmetric or not and to define the corresponding split number::

    bv:Vr/ParticleSplit/Symmetric = 2 "false" "true"
    uv:Vr/ParticleSplit/SplitNumber = 2 8 8

.. image:: geometrical_splitting.png

In addition for this technique, geometrical Russian roulette will be played if a particle outs to the component or to the world in a scheme similar to the Geant4 importance sampling technique described below.
