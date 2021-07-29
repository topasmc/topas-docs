Random Number Seed
------------------

To set the random seed::

    i:Ts/Seed = 1 # default is 1

To generate several statistically independent runs, give each run a different ``Ts/Seed``.
A typical solution to produce 10 independent runs would be to give starting seeds of 1 to 10. The allowed range is 0 to 2147483647 (the maximum 32 bit integer).

For more details see the discussion in the `Geant4 Application Developer's Guide <http://geant4.web.cern.ch/geant4/UserDocumentation/UsersGuides/ForApplicationDeveloper/html/ch03s02.html#sect.GlobClass.HEPRandom>`_.

We use the random engine called ``RanecuEngine`` and the seed given to TOPAS is passed to the engine through ``CLHEP::HepRandom::setTheSeed``.


How to save and reuse random seed of a problematic history:
-----------------------------------------------------------

When a rare issue is to be debugged, it is easier if one can make the simulation start
immediately from the problematic history.
To do this, one needs to know the seed number of that particular history.
But if this issue causes a crash, it is then too late then to ask TOPAS to write out the seed.

For a given history number, TOPAS can quickly find you the appropriate seed,
which you can then use in a subsequent job to start out right from the relevant history.

Set the parameter::

    i:Ts/FindSeedForHistory = 9998 # defaults to -1, meaning do not activate this feature

And if you have multiple Runs::

    i:Ts/FindSeedForRun = 0 # defaults to 0

When you then run TOPAS, it will "fast forward" through a simulation to get just that history's seed.
It skips most of the time-consuming parts of the simulation.
Its only job is to find and write out the random seed.
The seed information will be written to the console, and will also be written to a "seed file" such as:

* TopasSeedForRun_0_History_9998.txt

This simulation will not be useful for anything else, but it will be very fast.
TOPAS will:

* Disable graphics
* Disable GUI
* Set physics to transportation_only
* Disable setting of cuts
* Disable variance reduction
* Disable generators
* Disable most UpdateForNewRun functions

You can then set up a fresh, normal TOPAS session that will starts right from the desired history.
To do so, remove that FindSeedForHistory parameter, and tell TOPAS to use the saved seed file::

    s:Ts/SeedFile = "TopasSeedForRun_0_History_9998.txt" # Seed file saved in fast-forward job above

If the seed file is not in the current directory, you can also specify a seed file directory::

    s:Ts/SeedDirectory = "/Applications/tswork/testarea/SkipUntil" # defaults to read from current directory
