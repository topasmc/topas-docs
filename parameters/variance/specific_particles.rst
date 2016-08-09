Tracking Only Specific Particles
--------------------------------

In this option the particles are eliminated just after they were created. The user can chose which particles will be tracked in all components. Nevertheless, user can specifies if any component is going to be avoid. That is, all particles are tracked in such components. This option can be useful when the contribution of certain particles is negligible to the final scored quantity. But it must to be used with careful. This option is not a variance reduction.

To eliminate particles different than protons and electrons in all components but in component named water phantom::

    b:Vr/KillOtherParticles/Active = "True"
    sv:Vr/KillOtherParticles/HaveNoEffectInComponentsNamed = 1 "WaterPhantom"
    sv:Vr/KillOtherParticles/OnlyTrackParticlesNamed = 2 "proton" "e-"
