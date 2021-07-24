.. _source_distributed:

Distributed Source
------------------

The Distributed source represents radioactive material randomly distributed within other material.
The user specifies how many random source points to sample within the component.
The particle generator will then start equal numbers of histories from each of these source points.

The Distributed Source is in many ways similar to the Volumetric Source.
But whereas the Volumetric Source samples a new point every time it generates a particle
(to simulate random activity within a volume of radioactive material),
the Distributed Source does this sampling only a the construction phase
(to simulate a random distribution of radioactive particles within some other material).

Specify source type as::

    s:So/Example/Type = "Volumetric"

Additional required Parameters for the Distributed Source are::

    s:So/Example/Component = "DemoSphere"
    i:So/Example/NumberOfHistoriesInRun = 5
    i:So/Example/NumberOfSourcePoints = 4
    b:So/Example/RedistributePointsOnNewHistory = "False"
    s:So/Example/PointDistribution = "Gaussian" # default to "Flat"
    d:So/Example/PointDistributionSigma = 20. mm

And then the usual other parameters to control particle type, energy, etc., such as:

    s:So/Example/BeamParticle = "gamma"
    d:So/Example/BeamEnergy = 10. keV
    u:So/Example/BeamEnergySpread = 0.

Examples that use this source can be found in:

* examples/Basic/DistributedSourcePointsInShell.txt
* examples/Basic/DistributedSourcePointsInSphere.txt
* examples/Basic/DistributedSourcePointsInSphereGaussian.txt
* examples/Basic/DistributedSourcePointsInTwistedTubs.txt
