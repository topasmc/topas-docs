Miscellaneous
-------------


.. _scoring_binning_space:

Binning in Dividable Components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When scoring in :ref:`geometry_dividable` (TsBox, TsCylinder or TsSphere), you have many binning options. By default, binning will match the divisions of the volume. So if you have divided the component, the score will be divided in the same manner.

You are also free to specify some other binning.

* In a TsBox, you can specify binning in X, Y and Z::

    i:Sc/MyScorer/XBins = 512
    i:Sc/MyScorer/YBins = 512
    i:Sc/MyScorer/ZBins = 256

* In a TsCylinder, you can specify binning in R, Phi and Z::

    i:Sc/MyScorer/RBins = 100
    i:Sc/MyScorer/PhiBins = 20
    i:Sc/MyScorer/ZBins = 1

* In a TsSphere, you can specify binning in R, Phi and Theta::

    i:Sc/MyScorer/RBins = 20
    i:Sc/MyScorer/PhiBins = 20
    i:Sc/MyScorer/ThetaBins = 1

Behind the scenes, TOPAS uses Geant4’s parallel worlds system to support this binning flexibility. When scoring binning is different from the component's natural binning, TOPAS actually scores in a parallel world copy of the component. This is all done automatically.

Because TOPAS is a fully 3D code, letting you design beams to come from any side, bin 0 may be the first bin hit by the beam, but may also be the last bin hit by the beam. So do not be surprised if beam profiles are the opposite of what you might have expected.
If it is important to you that bin 0 be the first bin hit,
you may need to change your beam position and direction,
or rotate your scoring component by 180 degrees.



.. _scoring_binning_energy:

Binning by Energy
~~~~~~~~~~~~~~~~~

Any scorer can be binned by particle energy, by adding the following parameters::

    i:Sc/MyScorer/EBins = 10 # defaults to 1, that is, un-binned
    d:Sc/MyScorer/EBinMin = 0. MeV # defaults to zero
    d:Sc/MyScorer/EBinMax = 100. MeV # must be specified if EBins is greater than 1

Note that there are several options for what me mean here by "particle energy."

From our proton therapy dose calculation roots, the energy binning that we do by default is based not on the energy of the final particle at hit deposition time but instead on the incident particle energy.
This is the energy of the final scored particle, or its ancestor, when that particle or ancestor was first incident on the scoring volume.

However, users who have been trying to use this feature to get a spectrum instead need the particle's energy at the current step.

So we have now have a parameter to control what kind of Energy we use for this binning.::

    s:Sc/MyScorer/EBinEnergy = "IncidentTrack" # "IncidentTrack", "PreStep" or "DepositedInStep"
    
* "IncidentTrack" is the behavior we have had in the past, the energy that the particle or its ancestor had when it first was incident on the scoring component. This remains the default.
* "PreStep" is the track's energy at the start of the current step.
* "DepositedInStep" is the amount of energy deposited in the current step.

An example shows the effect of the three different choices:

    examples/Scoring/EnergyDepositBinnedByEnergy.txt

The output will include two extra bins, one for underflow (energy < ``EBinMin``), one for overflow (energy > ``EBinMax``). And if you have set EBinEnergy to IncidentTrack, there will be one more bin to hold those deposits for which there is no incident track (the primary particle was created already inside the scoring component, so neither it nor any ancestor of it was ever incident upon the scoring component).



.. _scoring_binning_time:

Binning by Time
~~~~~~~~~~~~~~~

Any scorer can be binned by time-of-flight, the elapsed time since the history was generated (in Geant4 this is called "global time")::

    i:Sc/MyScorer/TimeBins = 10 # defaults to 0, that is, un-binned
    d:Sc/MyScorer/TimeBinMin = 0. ns # defaults to zero
    d:Sc/MyScorer/TimeBinMax = 100. ns # must be specified if TimeBins is greater than 1

The output will include two extra bins, one for underflow (time < ``TimeBinMin``) and one for overflow (time > ``TimeBinMax``). Note that this time-of-flight is not the same as the TOPAS time feature time. To split results based on that TOPAS time, see :ref:`scoring_time_split`.

When radioactive decay is present, some very large times can occur, as decay may be delayed for hours or days. Thus it is not unusual to have some times exceed the ``TimeBinMax``. To get an interesting report on what particles and processes exceed ``TimeBinMax``, set ``Ts/TrackingVerbosity > 0``.



.. _scoring_time_split:

Splitting by Time Feature
~~~~~~~~~~~~~~~~~~~~~~~~~

To split a scorer into separate scorers depending on the current value of any selected :ref:`Time Feature <time_feature>`::

    s:Sc/MyScorer/SplitByTimeFeature = some_time_feature_name

If the time feature is a Step function, one split scorer is made for each of the time feature's values. If the time feature is a Continuous function, another parameter is expected to specify split values. This will be either a dimensioned double vector, unitless vector or integer vector, depending on the type of controlling time feature, such as::

    dv:Sc/DoseAtPhantom/SplitByTimeFeatureValues = 5 0. 90. 180. 270. 360. deg

**Example 1** - Splitting under control of a Step Time Feature

To split up a 4D CT simulation's dose output depending on the CT time slice, where the CT time slice is controlled by::

    s:Tf/ImageName/Function = "Step"
    sv:Tf/ImageName/Values = 3 "image1" "image2" "image3"

The following will make the scorer ``DoseAtPhantom`` split by current value of ``Tf/ImageName/Value``::

    s:Sc/DoseAtPhantom/SplitByTimeFeature = "ImageName"

creating one scorer for each value of ``ImageName``::

    Sc/DoseAtPhantom-image1
    Sc/DoseAtPhantom-image2
    Sc/DoseAtPhantom-image3

**Example 2** - Splitting under control of a Continuous Time Feature

To split up a simulation's dose output depending on the position of a propeller, where the propeller position is controlled by::

    s:Tf/PropellerRotation/Function = "Linear deg"

The following will make ``DoseAtPhantom`` split by current value of ``Tf/PropellerRotation/Value``::

    s:Sc/DoseAtPhantom/SplitByTimeFeature = "PropellerRotation"
    dv:Sc/DoseAtPhantom/SplitByTimeFeatureValues = 5 0. 90. 180. 270. 360. deg

creating one scorer for each defined range of ``PropellerRotation``::

    Sc/DoseAtPhantom-0.-90.deg
    Sc/DoseAtPhantom-90.-180.deg
    Sc/DoseAtPhantom-180.-270.deg
    Sc/DoseAtPhantom-270.-360.deg

See the :ref:`example_scoring_timefeature` and :ref:`example_dicom_time` examples.



Statistical Information
~~~~~~~~~~~~~~~~~~~~~~~

By default, scorers will report the sum of the scored quantity over all histories, but many additional reporting options are available::

    sv:Sc/MyScorer/Report = 1 "Sum" # One or more of Sum, Mean, Histories, Count_In_Bin, Second_Moment, Variance, Standard_Deviation, Min, Max

Output columns will be in the same order as the values in the ``Report`` parameter.

When there is binning by energy or time, and there is more than one ``Report`` option (such as ``"Sum"`` and ``"Mean"``), the output will be ordered as:

* Sum (underflow), Mean (underflow), Sum (bin 1), Mean (bin 1), Sum (bin 2), Mean (bin 2), etc.

``"Histories"`` is the total number of histories that were simulated while this scorer was active (that is, excludes any histories that were produced when this scorer was gated to inactive).

``"Count_In_Bin"`` is the number of histories that contributed to this bin (that is, excludes any histories for which no particles hit this bin).

If only ``"Sum"`` is requested, simple accumulation is used.
If ``"Mean"``, ``"Second_Moment"``, ``"Variance"`` or ``"Standard_Deviation"`` is requested, accumulation uses a numerically stable algorithm from:
Donald E. Knuth (1998). The Art of Computer Programming, volume 2: Seminumerical Algorithms, 3rd edn., p. 232. Boston: Addison-Wesley:

.. code-block:: plain

    for x in data:
        n = n+1
        delta = x - mean
        mean = mean + delta/n
        M2 = M2 + delta*(x - mean)
    sum = n * mean
    variance = M2/(n - 1)
    standard deviation = sqrt(variance)

Note that if your geometry has many divisions (such as the 70M voxels of a 512 x 512 x 256 CT), and you ask for ``"Mean"``, ``"Second_Moment"``, ``"Variance"`` or ``"Standard_Deviation"``, you will see a speed penalty. This occurs because any bin that has ever been hit will then have to recalculate its mean or second moment to account for the new history (even if the current history doesn't hit this bin).

TOPAS calculates the variance (and hence the standard deviation) associated with the distribution of the quantity of interest (dose, fluence, etc).

* For the standard deviation of the mean value, divide the standard deviation from TOPAS by the square root of the total number of histories.
* For the standard deviation of the sum, multiply the standard deviation from TOPAS by the square root of the total number of histories.



Change Component Color Based on Scoring
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can make TOPAS recolor a component during simulation to reflect a scored value. Using this technique, you can, for example, make a box become darker as it accumulates dose. See the :ref:`example_timefeature_darkening` example.

To activate this feature::

    s:Sc/EnergyInPhantom/ColorBy = "Sum" # sum, mean, histories, standard_deviation, min, max

You must then provide a list of colors, and cutoff values, such as::

    sv:Sc/EnergyInPhantom/ColorNames = 5 "white" "grey240" "grey220" "grey200" "grey180"
    dv:Sc/EnergyInPhantom/ColorValues = 4 1. 1000 2000 3000 MeV

In the above example:

* if the total energy is from 0 to 1, the phantom will be colored ``"White"``.
* if the total energy is from 1 to 1000, the phantom will be colored ``"grey240"``.
* if the total energy is from 1000 to 2000, the phantom will be colored ``"grey220"``.
* etc.

This feature must be used in conjunction with :ref:`time_feature`, as the color will only update after each run. And your scorer must be set to output after each run::

    b:Sc/EnergyInPhantom/OutputAfterRun = "True"

This technique does not currently work in the :ref:`geometry_dividable` (TsBox, TsCylinder and TsSphere). We will add this capability in a future TOPAS release. For now it only works in simple components made of single Geant4 solids.

.. todo:: Allow coloring based on scoring for dividable components



Toggling a Scorer Off and On
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To turn off a scorer::

    b:Sc/MyScorer/Active = "False" # defaults to "True"

This feature can be combined with boolean :ref:`time_feature` to produce gated scoring.
If the scorer skipped any values due to being set inactive at any time, the total number of skipped values is written out at in the scoring summary.



Restoring Results from Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TOPAS provides an option to read back scored values so that you can then redo the scoring output with different options. Set the parameter::

    Ts/RestoreResultsFromFile = "True" # defaults to "False"

With this set, simulation will not be run, but instead the scored values will be restored from the output of previous TOPAS simulations. For each scorer, there must be an appropriate file to read back, specified by name and type::

    s:Sc/MyScorer1/InputFile = "MySavedFileName" # match exact case
    s:Sc/MyScorer1/InputType = "csv"

The file to read back in must contain the appropriate scored quantity, the appropriate binning, and sufficient information to provide the new ``Report`` options. So, for example, if you previously scored ``"Sum"`` and ``"Histories"``, you could now report ``"Sum"``, ``"Mean"``, ``"Histories"``, and a DVH.

This option is particularly handy if you have been using Outcome Modeling.
You can run additional Outcome Model calculations, or repeat previous calculations with different model parameters,
without having to repeat the full simulation.

This option can also be used to read in binary output and write out csv, or vice versa.
