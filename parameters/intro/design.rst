.. _design:

Design Philosophy
-----------------

TOPAS follows a consistent set of design paradigms. Understanding these paradigms will make TOPAS more intuitive to you.

All control is through the :ref:`TOPAS Parameters System <parameters_intro>`. Use of Geant4 macros or interactive commands is not supported as it does not give you the reliability and repeatability that comes from the parameters system.

* TOPAS Parameter files are not Geant4 macro files. TOPAS is specifically designed to avoid the kind of order-dependence risks that Geant4 macro files create.
* TOPAS Parameter files are not XML files. Those too involve the kind of order dependence that we explicitly avoid.

To keep OpenGL graphics from vanishing from the screen, you have the option to have TOPAS pause at the Geant4 command line by including the option::

    b:Ts/PauseBeforeQuit = "True" # defaults to "False"

To exit the Geant4 command line, and continue with the TOPAS session, type ``exit``. For simulations that do not involve OpenGL graphics, just leave this option at ``"False"``.

All positions are set relative to :ref:`Geometry Components <geometry>`. If you want to place a particle source or a scorer, you place it relative to a particular Component. You may choose to do your placement relative to the center of the World component, in which case you have essentially used the global coordinate system, but you will likely choose a more directly relevant Component. For example, a source that represents a particle beam might be placed at the beamline exit window. Doing so means that the source position will move appropriately with any nozzle movement.

All time dependent behaviors are controlled through the :ref:`time_feature` system.

TOPAS fully supports the Multi-Threaded simulation capability of Geant4. By default, TOPAS will occupy just one CPU thread, but you can spread the simulation over multiple threads, distributing the load over your entire computer, by adjusting the parameter ``i:Ts/NumberOfThreads``. See details in the section :ref:`multithreading`.
