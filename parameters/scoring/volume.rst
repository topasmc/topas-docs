.. _scoring_volume:

Volume Scorers
--------------

Here are the available volume scorers:

==================  =======================================
Quantity            Description
==================  =======================================
DoseToMedium        sum of energy deposits divided by mass
DoseToWater         from energy-dependent stopping power conversion (see below)
DoseToMaterial      from energy-dependent stopping power conversion (see below)
EnergyDeposit       sum of step lengths divided by volume
Fluence             sum of step lengths times energy divided by volume
EnergyFluence       counting method described below
Charge              counting method described below
OpticalPhotonCount  counting optical photons
EffectiveCharge
StepCount
ProtonLET           various methods described below
==================  =======================================

Volume Scorers must indicate the relevant ``Component``::

    s:Sc/MyScorer/Component = "Phantom"

For DoseToMaterial, you must also specify the ``Material``::

    s:Sc/MyScorer/Material = "SomeMaterial"

Note that in this case, the material name must exactly match the case defined in Geant4.  To check what materials have been defined, add the parameter::

    i:Ma/Verbosity = 1

For DoseToWater and DoseToMaterial, we use energy-dependent stopping power conversion as in:

.. code-block:: c++

    dose_to_new_material = dose_to_medium * ( density_of_medium / density_of_new_material ) * ( dEdX_in_new_material / dEdX_in_medium )

The ``dEdX`` comes from the Geant4 ``EmCalculator`` utility.

The DoseToWater and DoseToMaterial scorers are somewhat slow since, for every hit, they need to compute stopping power ratios based on the current energy of the particle.
You can obtain better speed by adding the option::

    b:Sc/MyScorer/PreCalculateStoppingPowerRatios = "True" # defaults to "False"

* False gives the best accuracy, calculating stopping power on-the-fly for the exact energy.
* True gives the best speed, looking up stopping power from a pre-calculated table binned by energy. It is about 50% faster than the default option for typical patient simulations. The difference in accuracy is not significant for most studies.

For ``PreCalculateStoppingPowerRatios``, the table of stopping power ratios can be tuned by::

    Sc/MyScorer/ProtonEnergyBinSize # default is 1 MeV
    Sc/MyScorer/MinProtonEnergyForStoppingPowerRatio # default is 1 MeV
    Sc/MyScorer/MaxProtonEnergyForStoppingPowerRatio # default is 500 MeV
    Sc/MyScorer/ElectronEnergyBinSize # default is 1 keV
    Sc/MyScorer/MinElectronEnergyForStoppingPowerRatio # default is 1 keV
    Sc/MyScorer/MaxElectronEnergyForStoppingPowerRatio # default is 1 MeV

For Charge and EffectiveCharge:

* If a particle reaches zero kinetic energy in the scoring volume, its charge is accumulated
* If a particle is generated in the scoring volume, its charge is subtracted



ProtonLET Scorer
~~~~~~~~~~~~~~~~

The ProtonLET scorer gives the LET of primary and secondary protons, including the energy deposited by associated secondary electrons. It uses techniques discussed in two recent articles on best practices to score LET in Geant4:

* Phys. Med. Biol. 60 (2015) 2645–2669 by MA Cortes-Giraldo and A Carabe
* Phys. Med. Biol. 60 (2015) N283–N291 by DA Granville and GO Sawakuchi

In particular, we adopt the methods developed by Granville and Sawakuchi.
We compute dose-averaged LET, but you may instead request track-averaged::

    s:Sc/MyScorer/WeightBy = "Track" # defaults to "Dose"

By default, the LET is computed by dividing the energy deposited by the step length. Such distributions can feature spurious spikes, caused by events where the step length is severely constrained by a voxel boundary crossing. Three solutions to this issue are provided:

* By default, a step-by-step upper cut-off is set, such that steps contributing greater than this value are not be scored::

    d:Sc/MyScorer/MaxScoredLET = 100 MeV/mm/(g/cm3) # default 100 MeV/mm/(g/cm3)

* Alternately, you can set the LET computation to look up the electronic stopping power for the pre-step proton energy::

    b:Sc/MyScorer/UsePreStepLookup = "True" # defaults to “False”

* Or you can increase the electron production threshold::

    d:Ph/Default/CutForElectron = 1 mm # defaults to 0.05 mm

The ProtonLET Scorer can give values that are too high in air, where the mean path length between discrete processes can be larger than the voxel size. This can be avoided by neglecting secondary electrons, with::

    d:Sc/MyScorer/NeglectSecondariesBelowDensity = 0.1 g/cm3

Even when you do this, rare events that produce very low energy protons (e.g. a recoiling hydrogen nucleus) will produce spikes in LET. This is also seen in the ``PreStepLookup`` version of the scorer. They are not seen in the fluence-averaged version of the scorer, since they are rare events. For this reason we introduce the parameter::

    d:Sc/MyScorer/UseFluenceWeightedBelowDensity = 0. g/cm3

We set this to zero by default because it is strange to mix both types of LET in a single distribution, and could be significantly wrong at the end of range. We expect users to want to enable this when making a pretty plot of LET to overlay on a CT scan, without spikes in cavities and outside the patient.
