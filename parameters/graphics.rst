Graphics
========

You may have zero, one or more graphics active at same time::

    s:Gr/MyGraphic1/Type = "OpenGL" # OpenGL, HepRep, VRML, DAWN, RayTracer, RayTracerX

Note that the file-based graphics systems, HepRep, VRML and DAWN may not show any image until at least one history is run. We will revisit this issue when we move to the next Geant4 version.

HepRep files are designed to be viewed in a Java application called HepRApp.
Details can be found `here <http://geant4.slac.stanford.edu/Presentations/vis/G4HepRAppTutorial/G4HepRAppTutorial.html>`_.

Note that graphics can be one of the slowest parts of a simulation, so should be disabled if you are running a long simulation. To disable graphics, do one of the following three things:

* Comment out all of the ``Gr/*/Type`` parameters
* Set all ``Gr/*/Active`` to "False"
* Disable graphics entirely, by setting: ``b:Gr/Enable = "False"``

This last option is essential of you want to run on a batch system that does not contain any OpenGL graphics drivers.

File-based graphics systems will also expect a file name::

    s:Gr/MyGraphic1/FileName = "MyFileName" # Defaults to name of view (which here is MyGraphic1).

Will use this filename plus an "_n" where n increments with each refresh.
Due to limitations in Geant4, only affects OpenGL and HepRep. For other cases, the file name is a fixed value, ``g4_`` followed by a file number.

This can be more than just a file name - it can include a relative or absolute file path, as in::

    s:Gr/MyGraphic1/FileName = "../MyFileName" # one directory above current directory
    s:Gr/MyGraphic1/FileName = "~/SomeSubdirectory/MyFileName"

Basic options::

    b:Gr/MyGraphic1/IncludeGeometry = "True" # defaults to "True"
    b:Gr/MyGraphic1/IncludeTrajectories = "True" # defaults to "True"
    b:Gr/MyGraphic1/IncludeStepPoints = "True" # Show trajectory step points, defaults to "False"

Colors are defined by specifying their red, green, blue components, each on a scale of 0 to 255, as in::

    iv:Gr/Color/lightblue = 3 175 255 255

By default, trajectories will be drawn as what Geant4 calls "Smooth Trajectories", which means they include additional points to make them curve smoothly in a magnetic field. Geant4 does not actually use these "auxiliary points" in its simulation results, they are just present to make visualization in a field look better. In some cases, Geant4 has trouble handling these auxiliary points, and reports:  ``!!!!!!!! Filter: auxiliary points are being memory leaked !!!!!``
To work around this, turn off trajectory drawing or tell Geant4 not to making the trajectories smooth::

    b:Gr/MyGraphic1/UseSmoothTrajectories = "False" # defaults to "True"

You can add axes to the display. Axes lines are colored red for X, green for Y, blue for Z::

    b:Gr/MyGraphic1/IncludeAxes = "True" # defaults to "False"
    s:Gr/MyGraphic1/AxesComponent = "World" # Component in which to center the axes. Defaults to World.
    d:Gr/MyGraphic1/AxesSize = 3. m # size of axes

Note that on most OpenGL graphics systems, the shadowing on the arrowheads allows you to tell whether a given axis is coming towards or away from you.

You can visualize magnetic fields, with field intensity and direction depicted through a set of arrows::

    i:Gr/ViewA/MagneticFieldArrowDensity = 10

Use with caution. When combined with rotation seems to sometimes cause crashes in polycone drawing (involved in drawing the arrowheads).

By default, graphics views will refresh after every run. But you can change this to show each history individually or to accumulate all histories for the entire session (multiple runs) with::

    s:Gr/RefreshEvery = "History" # "History", "Run" or "Session"

If parallel worlds are present, by default they will be visible. If you instead want to see only the main world, specify::

    sv:Gr/MyGraphic1/VisibleWorlds = 1 "World" # "World", "All" or one or more specific world names

To turn off a graphic::

    b:Gr/MyGraphic1/Active = "False" # defaults to "True"

Extra options used by OpenGL::

    u:Gr/MyGraphic1/Zoom = 2. # increase to zoom in, decrease to zoom out
    d:Gr/MyGraphic1/Theta = 45. deg # view angle as in /vis/viewer/set/viewpointThetaPhi
    d:Gr/MyGraphic1/Phi = 45. deg # view angle as in /vis/viewer/set/viewpointThetaPhi
    u:Gr/MyGraphic1/TransX = 0. # move left or right in the view window
    d:Gr/MyGraphic1/TransY = 0. # move up or down in the view window
    s:Gr/MyGraphic1/Projection = "Perspective" # Defaults to "Orthogonal"
    d:Gr/MyGraphic1/PerspectiveAngle = 10. deg # Increase for stronger perspective effect
    i:Gr/MyGraphic1/WindowSizeX = 600
    i:Gr/MyGraphic1/WindowSizeY = 600
    i:Gr/MyGraphic1/WindowPosX = 0
    i:Gr/MyGraphic1/WindowPosY = 0
    b:Gr/MyGraphic1/HiddenLineRemovalForGeometry = "False" # Remove hidden lines from wireframe geometries, like Geant4’s /vis/viewer/set/hiddenEdge
    b:Gr/MyGraphic1/HiddenLineRemovalForTrajectories = "False" # Remove hidden trajectories lines from within geometries, like Geant4’s /vis/viewer/set/hiddenMarker

You can set Topas so that each time the OpenGL updates, the view is copied to a file::

    b:Gr/MyGraphic1/CopyOpenGLToPDF = "True" # save to PDF
    b:Gr/MyGraphic1/CopyOpenGLToSVG = "True" # save to Scalable Vector Graphics
    b:Gr/MyGraphic1/CopyOpenGLToEPS = "True" # save to Encapsulated PostScript
    b:Gr/MyGraphic1/CopyOpenGLToPS = "True" # save to PostScript

Some views may result in one of the following warning messages from Geant4 Visualization.  These messages are just informational and can be safely ignored.

* "WARNING: Viewpoint direction is very close to the up vector direction.
  Consider setting the up vector to obtain definable behavior."
* "G4PhysicalVolumeSearchScene::FindVolume:
  Required volume "Phantom3_10x10x1", copy no. 0, found more than once.
  This function is not smart enough to distinguish identical physical volumes which have different parentage. It is tricky to specify in general. This function gives you access to the first occurrence only."

To create movies, Zoom, Theta, Phi, TransX, TransY, Projection and PerspectiveAngle can be controlled by time features.

Trajectory Coloring::

    s:Gr/MyGraphic1/ColorBy = "Charge" # "Charge", "ParticleType", "OriginComponent", "Energy", "Momentum", "Generation", "CreatorProcess"

For ColorBy = Charge, trajectories default to red, greed, blue for negative, neutral and positive.  You can override these defaults with::

    sv:Gr/MyGraphic1/ColorByChargeColors = 3 "blue" "green" "red" # colors for neg, neutral, pos

For ColorBy = ParticleType, colors are Geant4 defaults:

* gamma = green
* e- = red
* e+ = blue
* pi+- = magenta
* proton = cyan
* neutron = yellow
* other = grey

You can override these settings with (particle names are described :ref:`here <particle_names>`)::

    sv:Gr/MyGraphic1/ColorByParticleTypeNames = 4 "e-" "gamma" "proton" "neutron" # any number of particle names
    sv:Gr/MyGraphic1/ColorByParticleTypeColors = 4 "red" "green" "blue" "yellow" # for each particle type above. All other particles will be set to grey.

For ColorBy = OriginVolume, trajectories are grey unless they come from a named volume in::

    sv:Gr/MyGraphic1/ColorByOriginVolumeNames = 1 "Propeller20/Leaf" # one or more volume
    sv:Gr/MyGraphic1/ColorByOriginVolumeColors = 1 "red" # one color for each name above

For ColorBy = OriginComponent, trajectories are grey unless they come from a named component in::

    sv:Gr/MyGraphic1/ColorByOriginComponentNames = 1 "jaws" # one or more component names
    sv:Gr/MyGraphic1/ColorByOriginComponentColors = 1 "red" # one color for each name above

For ColorBy = ColorByOriginComponentOrSubComponentOf, trajectories are grey unless they come from a named component or any of its subcomponents in::

    sv:Gr/MyGraphic1/ColorByOriginComponentNames = 1 "Nozzle" # one or more components
    sv:Gr/MyGraphic1/ColorByOriginComponentColors = 1 "red" # one color for each name above

For ColorBy = Energy::

    dv:Gr/MyGraphic1/ColorByEnergyRanges = 3 1. 4. 8. MeV # limits of energy ranges
    sv:Gr/MyGraphic1/ColorByEnergyColors = 4 "red green blue yellow" # one for every energy interval that is defined by those ranges - one more value than number of ranges since includes less than first range value and greater than first range value

For ColorBy = Momentum::

    dv:Gr/MyGraphic1/ColorByMomentumRanges = 3 1. 4. 8. MeV # limits of momentum ranges
    sv:Gr/MyGraphic1/ColorByMomentumColors = 4 "red" "green" "blue" "yellow" # one for every energy interval that is defined by those ranges - one more value than number of ranges since includes less than first range value and greater than first range value

For ColorBy = Generation::

    sv:Gr/MyGraphic1/ColorByGenerationColors = 2 "red" "green" # colors for primary and secondaries

For ColorBy = CreatorProcess::

    sv:Gr/MyGraphic1/ColorByCreatorProcessNames = 5 "eBrem" "annihil" "Decay" "eIoni" "hIoni" # one or more process name
    sv:Gr/MyGraphic1/ColorByCreatorProcessColors = 5 "red" "green" "blue" "yellow" "magenta" # one for every process name

To control how often graphics refresh (applies globally to all graphics views)::

    s:Gr/RefreshEvery = "Run" # "History", "Run" or "Session"

To filter what trajectories will be in the graphics, use similar syntax to that used for filtering of scoring and particle source (apply globally to all graphics views)::

    sv:Gr/OnlyIncludeParticlesNamed = 2 "proton" "neutron" # one or more particle names
    sv:Gr/OnlyIncludeParticlesCharged = 1 "negative" # one or more "positive", "negative" or "neutral"
    sv:Gr/OnlyIncludeParticlesFromVolume = 1 "Propeller20/Leaf" # one or more volume
    sv:Gr/OnlyIncludeParticlesFromComponent = 1 "Jaws" # one or more component
    sv:Gr/OnlyIncludeParticlesFromComponentOrSubComponentsOf = 1 "Nozzle" one or more
    d:Gr/OnlyIncludeParticlesWithInitialKEBelow = 1. MeV # maximum energy
    d:Gr/OnlyIncludeParticlesWithInitialKEAbove = 10. MeV # minimum energy
    d:Gr/OnlyIncludeParticlesWithInitialMomentumBelow = 1. MeV # maximum momentum
    d:Gr/OnlyIncludeParticlesWithInitialMomentumAbove = 10. MeV # minimum momentum
    sv:Gr/OnlyIncludeParticlesFromProcess = 1 "hIoni" # one or more process name

Note that the following three filters may cause a crash if the particle origin is at the world boundary::

    sv:Gr/OnlyIncludeParticlesFromVolume
    sv:Gr/OnlyIncludeParticlesFromComponent
    sv:Gr/OnlyIncludeParticlesFromComponentOrSubComponentsOf

We will study this issue again when we move to the next Geant4 version.

Visualization control for a specific component is done as part of the Ge/ parameters for that component rather than in the ``Gr/`` parameters::

    s:Ge/MyComponent/Color = "red"
    s:Ge/MyComponent/DrawingStyle = "Solid" # "Solid", "Wireframe" or "FullWireFrame".
    # FullWireFrame includes drawing of additional edge lines that Geant4 calls "soft edges"
    # - on many graphics devices WireFrame and FullWireFrame give the same result
    i:Ge/MyComponent/VisSegsPerCircle = 100 # Number of line segments to use to approximate a circle, defaults to 24. Set to a larger number if you want a smoother curve
    b:Ge/MyComponent/Invisible = "True" # defaults to False meaning visible

We sometimes see error messages from visualization of the following form:

.. code-block:: plain

    G4PhysicalVolumeSearchScene::FindVolume:
    Required volume "PhantomCentralDose_1x1x40", copy no. 0, found more than once...

Such messages can be ignored. They do not affect the simulation results. We will revisit how to solve these error messages once we move to the next Geant4 version.
