Tracking Only Specific Particles
--------------------------------

In this option the particles are eliminated just after they were created. The user can choose which particles will be tracked in all components. Nevertheless, the user can specify if a component is going to be neglected. That is, all particles are tracked in such components. This option can be useful when the contribution of certain particles is negligible to the final scored quantity. But it must to be used with caution. This option is not a variance reduction.

To eliminate particles other than protons and electrons in all components but in component named ``WaterPhantom``::

    b:Vr/KillOtherParticles/Active = "True"
    sv:Vr/KillOtherParticles/HaveNoEffectInComponentsNamed = 1 "WaterPhantom"
    sv:Vr/KillOtherParticles/OnlyTrackParticlesNamed = 2 "proton" "e-"
