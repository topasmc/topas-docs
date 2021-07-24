.. _source_beam:

Beam Sources
------------

By default there is a single source named ``Demo`` centered on a Component named ``BeamPosition`` that is placed at one end of the ``World``. The beam shape is an Ellipse. Each of these parameters is described in detail below::

    s:So/Demo/Type = "Beam" # Beam, Isotropic, Emittance or PhaseSpace
    s:So/Demo/Component = "BeamPosition"
    s:So/Demo/BeamParticle = "proton"
    d:So/Demo/BeamEnergy = 169.23 MeV
    u:So/Demo/BeamEnergySpread = 0.757504
    s:So/Demo/BeamPositionDistribution = "Gaussian" # None, Flat or Gaussian
    s:So/Demo/BeamPositionCutoffShape = "Ellipse" # Rectangle or Ellipse (if Flat or Gaussian)
    d:So/Demo/BeamPositionCutoffX = 10. cm # X extent of position (if Flat or Gaussian)
    d:So/Demo/BeamPositionCutoffY = 10. cm # Y extent of position (if Flat or Gaussian)
    d:So/Demo/BeamPositionSpreadX = 0.65 cm # distribution (if Gaussian)
    d:So/Demo/BeamPositionSpreadY = 0.65 cm # distribution (if Gaussian)
    s:So/Demo/BeamAngularDistribution = "Gaussian" # None, Flat or Gaussian
    d:So/Demo/BeamAngularCutoffX = 90. deg # X cutoff of angular distrib (if Flat or Gaussian)
    d:So/Demo/BeamAngularCutoffY = 90. deg # Y cutoff of angular distrib (if Flat or Gaussian)
    d:So/Demo/BeamAngularSpreadX = 0.0032 rad # X angular distribution (if Gaussian)
    d:So/Demo/BeamAngularSpreadY = 0.0032 rad # Y angular distribution (if Gaussian)
    i:So/Demo/NumberOfHistoriesInRun = 0

Where the default definition of ``BeamPosition`` is::

    s:Ge/BeamPosition/Parent="World"
    s:Ge/BeamPosition/Type="Group"
    d:Ge/BeamPosition/TransX=0. m
    d:Ge/BeamPosition/TransY=0. m
    d:Ge/BeamPosition/TransZ= Ge/World/HLZ m
    d:Ge/BeamPosition/RotX=180. deg
    d:Ge/BeamPosition/RotY=0. deg
    d:Ge/BeamPosition/RotZ=0. deg

Details on ``BeamEnergySpread``:

* The number is unitless because we find it more convenient generally to speak of the spread in terms of percentage of the mean energy, rather than as an absolute number. We could have chosen either representation, but this one seemed most consistent with what we see from other beam modeling applications.
* This is a standard deviation. So the code we have is:

.. code-block:: c++

    fEnergySpread = BeamEnergySpread * fEnergy / 100.;
    p.kEnergy = CLHEP::RandGauss::shoot(fEnergy, fEnergySpread);

* So, for example, if you want a spread of 0.2 MeV, and your energy is 153 MeV, set ``BeamEnergySpread`` to:

.. code-block:: plain

    0.2 MeV / 153 MeV * 100 = 0.13

To run generate histories using this demo source, set its number of histories to some value::

    So/Demo/NumberOfHistoriesInRun = 10

We recommend that you not use ``So/Demo`` for any serious work. This demonstration source is just there for simple demonstrations. For any serious work, please define your own source so that you do not just accidentally inherit any of the characteristics of our ``Demo`` source. Source characteristics vary greatly from one application to another. There is no meaningful "default" value that we can set for you.

So when you set out on your own work, define a new source name, such as::

    s:So/MySource/BeamParticle = "proton"
    d:So/MySource/BeamEnergy = 200. MeV
    i:So/MySource/NumberOfHistoriesInRun = 100
    ...

You can provide an energy spectrum instead of a fixed energy by setting the following to ``"Discrete"`` or ``"Continuous"``::

    s:So/MySource/BeamEnergySpectrumType = "Continuous" # Either "None", "Discrete" or "Continuous"

and providing energies and weights as::

    dv:So/MySource/BeamEnergySpectrumValues = 3 50. 100. 150. MeV
    uv:So/MySource/BeamEnergySpectrumWeights = 3 .20 .60 .20

An example is in :ref:`example_basic_spectrum`.

Any source that has ``NumberOfHIstoriesInRun`` greater than zero will contribute primary particles.

The beam is emitted along the Z axis of the beam’s ``Component`` and may have some spread along the X and Y axes.

For ``Type = "Beam"``, the beam shape can be further described by a set of parameters that control the position distribution of the start of the beam::

    s:So/Demo/BeamPositionDistribution = "Gaussian" # None, Flat or Gaussian
    s:So/Demo/BeamPositionCutoffShape = "Ellipse" # Rectangle or Ellipse (if Flat or Gaussian)
    d:So/Demo/BeamPositionCutoffX = 10. cm # X extent of position (if Flat or Gaussian)
    d:So/Demo/BeamPositionCutoffY = 10. cm # Y extent of position (if Flat or Gaussian)
    d:So/Demo/BeamPositionSpreadX = 0.65 cm # X standard deviation (used only if Gaussian)
    d:So/Demo/BeamPositionSpreadY = 0.65 cm # Y standard deviation (used only if Gaussian)

and a set of parameters that control how the beam spreads out from that start position::

    s:So/Demo/BeamAngularDistribution = "Gaussian" # None, Flat or Gaussian
    d:So/Demo/BeamAngularCutoffX = 90. deg # X cutoff of angular distrib (if Flat or Gaussian)
    d:So/Demo/BeamAngularCutoffY = 90. deg # Y cutoff of angular distrib (if Flat or Gaussian)
    d:So/Demo/BeamAngularSpreadX = 0.0032 rad # X standard deviation of angular distribution (used only if Gaussian)
    d:So/Demo/BeamAngularSpreadY = 0.0032 rad # Y standard deviation of angular distribution (used only if Gaussian)

The ``Cutoff`` parameter is applied symmetrically.

You will note that for Gaussian beams, the position and angular distribution are controlled both by ``Spread`` and by ``Cutoff`` parameters. The ``Spread`` control the standard deviation of the Gaussian with zero mean (keep in mind that the position and orientation of the source is controlled by the parameter ``So//Component``), while the ``Cutoff`` cut off the tails (which would otherwise be infinite). Inside TOPAS, when the Gaussian formula generates a starting point outside of this cutoff, that starting point is rejected and instead the random function is thrown again until a value is found that is within the specified cutoff.

If your particle type is Optical Photon, additional parameters let you set the polarization::

    u:So/*/BeamPolarizationX
    u:So/*/BeamPolarizationY
    u:So/*/BeamPolarizationZ

If polarization is not set, the Beam will have a uniformly random polarization vector (perpendicular to the initial momentum).