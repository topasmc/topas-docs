Random Number Seed
------------------

To set the random seed::

    i:Ts/Seed = 1 # default is 1

To generate several statistically independent runs, give each run a different ``Ts/Seed``.
A typical solution to produce 10 independent runs would be to give starting seeds of 1 to 10. The allowed range is 0 to 2147483647 (the maximum 32 bit integer).

For more details see the discussion in the `Geant4 Application Developer's Guide <http://geant4.web.cern.ch/geant4/UserDocumentation/UsersGuides/ForApplicationDeveloper/html/ch03s02.html#sect.GlobClass.HEPRandom>`_.

We use the random engine called ``RanecuEngine`` and the seed given to TOPAS is passed to the engine through ``CLHEP::HepRandom::setTheSeed``.
