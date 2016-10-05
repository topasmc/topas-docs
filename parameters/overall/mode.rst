.. _time_mode:

Time mode
---------

If you do nothing special, TOPAS will do a single run with no time variation. We call this "Fixed Time Mode". Other available modes are "Sequential" and "Random".



.. _time_mode_fixed:

Fixed Time Mode
~~~~~~~~~~~~~~~

To run in Fixed Time Mode, just set your source’s ``NumberOfHistoriesInRun``, as in::

    i:So/MySource/NumberOfHistoriesInRun = 100

If your parameter files include :ref:`time_feature`, they will all be evaluated with time equals zero. To instead have them evaluated at a different fixed time, specify ``TimelineStart``, as in::

    d:Tf/TimelineStart = 10. s # defaults to zero

If you have more than one source, the run will continue until all sources have run all of their histories. For each Geant4 "beamOn", each source will get called, but only those that have more histories left to produce will actually produce any.



.. _time_mode_sequential:

Sequential Time Mode
~~~~~~~~~~~~~~~~~~~~

To have TOPAS do several runs at fixed time intervals, specify the start time, end time and number of sequential times, as in::

    d:Tf/TimelineStart = 0. s # defaults to zero
    d:Tf/TimelineEnd = 10. s # must be larger than TimelineStart
    i:Tf/NumberOfSequentialTimes = 100 # defaults to 1

TOPAS will divide the overall time, ``TimelineEnd - TimelineStart``, by ``NumberOfSequentialTimes`` and
perform runs at each of these intervals.

* The first run will be at time = ``TimelineStart``.
* The last run will be at time = ``TimelineEnd`` minus one interval.  That is, TOPAS will stop *before* it reaches ``TimelineEnd``.

So, in the example above:

* Run 0 will have Time = 0. s
* Run 1 will have Time = 0.1 s
* ...
* Run 99 will have Time = 9.9 s

At each of these intervals, your source will generate your indicated ``NumberOfHistoriesInRun``::

    i:So/MySource/NumberOfHistoriesInRun = 10

So, for example, if you have 100 intervals, and ``NumberOfHistoriesInRun = 10``, you will generate a total of 100 x 10 = 1000 histories.

To have TOPAS print time feature information to a log file and to the console::

    i:Tf/Verbosity = 2 # defaults to zero.
    # set to 1 to get time log (NbParticlesInTime.txt)
    # set to 2 to get detailed update messages

To implement **beam current modulation**, have your source’s ``NumberOfHistoriesInRun`` get its value from a time feature, as in::

    i:So/MySource/NumberOfHistoriesInRun = Tf/MyBCMTimeFeature/Value

By default, scorers will output just once, after the entire session. But if you wish to have separate output from specific runs::

    b:Sc/MyScorer/OutputAfterRun = "True" # set True to trigger output of scorer after this run

* If this is False, or not defined, we just output at the end of the simulation.
* If this is True, we output after every run.



.. _time_mode_random:

Random Time Mode
~~~~~~~~~~~~~~~~

Random Time Mode generates one history per run, with a randomly sampled time at each run. This has several uses.

* It allows one to sample time in a continuous fashion, so may show features that are obscured by Sequential Mode
* It provides a way to do a lower statistics run of what would have been a very long Sequential Mode job, yet still see aspects of the entire time interval, rather than just the first subset of the sequential times

To run in Random Time Mode, specify the ``TimelineStart`` and ``TimelineEnd``, turn on ``RandomizeTimeDistribution``, and set your source’s ``NumberOfHistoriesInRandomJob``, as in::

    b:Tf/RandomizeTimeDistribution = "True" # defaults to "False"
    d:Tf/TimelineStart = 0. s # defaults to zero
    d:Tf/TimelineEnd = 10. s # must be larger than TimelineStart
    i:So/MySource/NumberOfHistoriesInRandomJob = 1000 # defaults to 100

For each history, a random time will be sampled between ``TimelineStart`` an ``TimelineEnd``.

We keep the parameters that control random mode (``NumberOfHistoriesInRandomJob``) separate from those that control sequential mode (``NumberOfHistoriesInRun`` and ``NumberOfSequentialTimes``) so that you can easily switch between the two modes (by just switching ``RandomizeTimeDistribution``).

To implement **beam current modulation**, give your source a time-dependent ``ProbabilityOfUsingAGivenRandomTime``, as in::

    d:So/MySource/ProbabilityOfUsingAGivenRandomTime = Tf/MyBCMTimeFeature/Value



Fixed Time but with Very Large Number of Histories
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The maximum number of histories possible per run is limited by the size of some of Geant4's internal counters. If you need more than 10^9 histories at a fixed time, you can work around this limitation by breaking your session into multiple runs:

* Set ``Tf/NumberOfSequentialTimes`` to some value greater than 1
* No need to actually set ``TimelineStart`` or ``TimelineEnd`` (they both default to 0)

Your total number of histories will then be ``NumberOfSequentialTimes * NumberOfHistoriesInRun``.
