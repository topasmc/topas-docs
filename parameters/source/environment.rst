.. source_environment

Environment Source
------------------

Environment sources create an isotropic, uniform radiation field enclosing
the specified component.

A TOPAS environment is a radiation field that might be experienced, for
example, by a spacecraft in a radiation belt, or a robot (or, indeed
a human) in a damaged nuclear reactor.

A notional radiation "cavity" is created enclosing all volumes in a
component. The cavity is a sphere of radius R.  Primary particles are
generated on the surface of the sphere, directed inwards, following a
cosine angular distribution (Lambert's cosine law) relative to the inward
direction. This produces an isotropic, homogeneous, "omnidirectional flux".

Even if the radiation has some directional dependency it is often the case
that the instrument (your detector) is rotating or moving about so the
flux will average to isotropic over time.

The basic definition of flux, f, which in principle can vary with
direction and position, is defined by dN/dt = f*da*dOmega, the
rate of flow of particles out of an element of area da perpendicular to
the direction into an element of solid angle dOmega. If the flux is
homogenous and isotropic, we can define the "omnidirectional flux"
F = 4*pi*f per unit area. It is quoted, for example, as number per cm2
per second.

Fluence is simply F*T, the flux F over a time period T, so quoted, for
example, as number per cm2.

One can derive equivalent definitions of fluence:

- the number of particles that enter a sphere of unit cross-sectional
  area;
- the track length per unit volume.

For N particles (histories), the fluence will be N/(pi*R^2). This is
printed at the end of run. It is up to you to decide if this is enough
for your application. Thus:

- to simulate flux F for time T you need pi*R^2*F*T histories;
- or, given N histories, you will have simulated a time period
  T = N/(F*pi*R^2).

A test sphere of radius r will attract N*r^2/R^2 particles.

A thin test disc of radius r will attract (N/2)*r^2/R^2 particles.

Specify source type as::

  s:So/MySource/Type = "Environment"

See the example: examples/Basic/EnvironmentSource.txt.

Note: the world must be bigger than the radiation cavity, which may be
bigger than a box enclosing your geometry. TOPAS will tell you if you
need to increase the world size.

The energies and species of the emitted particles can be specified using the same parameters available to the Beam Sources.

