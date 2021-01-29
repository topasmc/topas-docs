Miscellaneous
-------------

Interactive Geant4 Sessions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To have TOPAS pause and wait for interactive Geant4 commands::

    b:Ts/PauseBeforeInit = "True"
    b:Ts/PauseBeforeSequence = "True"
    b:Ts/PauseBeforeQuit = "True"

After each pause, type the Geant4 command ``exit`` to return control to TOPAS.

* Most users will only use ``PauseBeforeQuit``, typically to make a graphics window stay open at the end of the session (graphics windows close when Geant4 quits).
* The other two options, ``PauseBeforeInit`` and ``PauseBeforeSequence``, provide the ability to enter Geant4 commands by hand, which may be useful in certain tests, but invalidates the basic TOPAS concept that the behavior of your simulation should be perfectly defined by TOPAS parameters.



Dump Parameter Values
~~~~~~~~~~~~~~~~~~~~~

Additional overall control parameters are::

    b:Ts/DumpParameters = "True" # dump full list of params to file TopasParameterDump_Run0.html
    b:Ts/DumpNonDefaultParameters = "False" # Like above but omits defaults
    sv:Ts/DumpParametersToSimpleFile = 2 "SomeParameter" "SomeOtherParameter" # Dumps the requested parameter types, names and values to a simple, human-readable file, TopasParameterDump_Run0.txt
    sv:Ts/DumpParametersToSemicolonSeparatedFile = 2 "SomeParameter" "SomeOtherParameter" # Dumps the requested parameter types, names and values to a semicolon separated file, TopasParameterDumpSSF_Run0.txt. This file is suitable for easy import into other applications



Verbosity
~~~~~~~~~

Additional overall control parameters are::

    i:Ts/ShowHistoryCountAtInterval = 1 # how often to print history count to the console
    # If set to 0, history count will never be printed
    b:Ts/ShowHistoryCountOnSingleLine = "False" # Make count reuse a single line of console
    i:Ts/TrackingVerbosity = 0 # Set to larger integer to see details of tracking

You can add time stamps to the history count:    b:Ts/IncludeTimeInHistoryCount = "True"

You can have a "power-based" history count:    b:Ts/ShowHistoryCountLessFrequentlyAsSimulationProgressesAfter first ten histories, output will change to once for every 10, then to once for every 100, etc.An additional optional parameter:

    i:Ts/MaxShowHistoryCountInterval

puts an upper limit on how high the ShowHistoryCountInterval can be.For example:    b:Ts/ShowHistoryCountLessFrequentlyAsSimulationProgresses    i:Ts/MaxShowHistoryCountInterval = 100Gives:
    1    2    3    ...    9    10    20    30    ...    100but from there always keep counting by 100 (rather than going on to counting by 1000, 10,000, etc.)



Other
~~~~~

Additional overall control parameters are::

    b:Ts/ShowCPUTime = "True" # Show CPU time used in various phases of the simulation
    i:Ts/RunIDPadding = 4 # Run numbers are padded in output files, such as MyScoringOutput_Run_0001.csv, so that they will sort naturally in various file viewers. This parameter sets how many places of padding are used.



Quick Ways to Deactivate Parts of the Parameters Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For most parameter categories, there is one key kind of parameter that triggers creation:

========================    =========================
Parameter object type       Triggering pattern
========================    =========================
Element                     ``El/.../Symbol =``
Material                    ``Ma/.../Components =``
Component                   ``Ge/.../Parent =``
Particle Source             ``So/.../Type =``
Physics setup               ``Ph/.../Type =``
Scorer                      ``Sc/.../Quantity =``
Graphic View                ``Gr/.../Type =``
Variance Reduction setup    ``Vr/.../Type =``
Time Feature                ``Tf/.../Function =``
========================    =========================

Thus you could effectively comment out the entire Component, Element, Material, Particle Source, etc. by just commenting out that line. But this way of turning something off can get you into trouble since you may then inherit behavior from a parent parameter file.

A better way to handle this is by setting a specific parameter designed for this purpose::

    Ge/MyComponent/Include = "False"
    So/MySource/NumberOfHistoriesInRun = 0
    Sc/MyScorer/Active = "False"
    Gr/MyGraphics/Active = "False"

Such a parameter can then even be controlled by a time feature.
