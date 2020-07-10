.. _parameters_default:

Index To Parameters
==================

This index is intended to list all of the parameters used by TOPAS (though we may have missed a few).
Clicking on any of these parameters will bring you to the relevant part of the TOPAS User Guide (links not finished yet).



TOPAS Overall Control
~~~~~~~~~~~~~~~~~~~~~

::

    i:Ts/Seed = 1 # starting random seed
    i:Ts/MaxStepNumber = 1000000 # limit on number of steps before a track is killed
    i:Ts/MaxInterruptedHistories = 10 # limit on how many histories can throw rare Geant4 errors
    b:Ts/DumpParameters = "False" # Set true to dump full set of parameters to html file TopasParameterDump_Run0.html
    b:Ts/DumpNonDefaultParameters = "False" # Like above but omits defaults
    b:Ts/ListUnusedParameters = "False" # Set true to list unused parameters on the console
    i:Ts/ShowHistoryCountAtInterval = 1 # How often to print history count to the console
    b:Ts/ShowHistoryCountLessFrequentlyAsSimulationProgresses = "False" # Counts by 1, then by 10, then by 100, etc.
    i:Ts/MaxShowHistoryCountInterval = "2147483647" # Stops increasing count interval after this limit
    b:Ts/ShowHistoryCountOnSingleLine = "False" # Set true to make history count reuse same line of console
    b:Ts/IncludeTimeInHistoryCount = "False" # Adds time stamp to history count
    i:Ts/RunIDPadding = 4 # pad Run ID numbers to this many places in file names
    b:Ts/PauseBeforeInit = "False" # Pause for Geant4 commands before initialization
    b:Ts/PauseBeforeSequence = "False" # Pause for Geant4 commands before run sequence
    b:Ts/PauseBeforeQuit = "False" # Pause for Geant4 commands before quitting
    i:Ts/RunVerbosity = 0 # Set to larger integer to see details of run. Maximum is 2
    i:Ts/EventVerbosity = 0 # Set to larger integer to see details of event. Maximum is 5
    i:Ts/TrackingVerbosity = 0 # Set to larger integer to see details of tracking
    i:Ts/SequenceVerbosity = 0 # Set to larger integer to see details of TOPAS run sequence
    b:Ts/QuitIfManyHistoriesSeemAnomalous = "True" # Quits if Geant4 warnings issued on too many histories
    i:Ts/NumberOfAnomalousHistoriesToAllowInARow = 10000 # Limit for above
    b:Ts/RestoreResultsFromFile = "False" # Re-reads previous results to allow new output format or outcome modeling
    i:Ts/NumberOfThreads = 1 # Number of CPU threads to which work will be distributed
    b:Ts/BufferThreadOutput = "False" # Causes console output to be show one thread at a time
    b:Ts/TreatExcitedIonsAsGroundState = "False" # Allows you to read back in excited ions in a phase space file
    s:Ts/G4DataDirectory = "" # Specify path to Geant4 Data files (instead of having to set environment variable)



Time Features
~~~~~~~~~~~~~

::

    b:Tf/RandomizeTimeDistribution = "False" # Causes each history to be at a different time sampled from timeline
    d:Tf/TimelineStart = 0. s
    d:Tf/TimelineEnd = Tf/TimelineStart s
    i:Tf/NumberOfSequentialTimes = 1
    i:Tf/Verbosity = 0 # set to 1 to generate time log, set to 2 to get detailed update messages



Geometry Overall Control
~~~~~~~~~~~~~~~~~~~~~~~~

::

    b:Ge/CheckForOverlaps = "True"
    b:Ge/CheckInsideEnvelopesForOverlaps = "False" # Speeds up checking by assuming inner parts of components are OK
    i:Ge/CheckForOverlapsResolution = 1000
    d:Ge/CheckForOverlapsTolerance = 0. mm
    b:Ge/QuitIfOverlapDetected = "True"
    i:Ge/NumberOfPointsPerOverlapCheck = 100
    b:Ge/CheckForUnusedComponents = "True"



Geometry Parameters Used by All Components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    s:Ge/\<ComponentName\>/Type = "TsBox"
    s:Ge/\<ComponentName\/Parent = "World"
    s:Ge/\<ComponentName\>/Material = "Air"
    d:Ge/\<ComponentName\>/TransX = 0. m
    d:Ge/\<ComponentName\>/TransY = 0. m
    d:Ge/\<ComponentName\>/TransZ = 0. m
    d:Ge/\<ComponentName\>/RotX = 0. deg
    d:Ge/\<ComponentName\>/RotY = 0. deg
    d:Ge/\<ComponentName\>/RotZ = 0. deg
    b:Ge/\<ComponentName\/Include = "False" # defaults to "True"
    d:Ge/\<ComponentName\/MaxStepSize = 1. mm # sets maximum step size used in this component
    i:Ge/\<ComponentName\>/CheckForOverlapsResolution = 1000
    d:Ge/\<ComponentName\>/CheckForOverlapsTolerance = 0. mm



Geometry Parameters for Component Type TsBox
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    d:Ge/\<ComponentName\>/HLX = 5. m # Half Length
    d:Ge/\<ComponentName\>/HLY = 5. m
    d:Ge/\<ComponentName\>/HLZ = 5. m



Geometry Parameters for Component Type TsSphere
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    d:Ge/\<ComponentName\>/RMax = 5. m
    d:Ge/\<ComponentName\>/RMin = 0. m
    d:Ge/\<ComponentName\>/DPhi = 0. deg
    d:Ge/\<ComponentName\>/SPhi = 180. deg


Particle Source Parameters Used by All Source Types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    s:So/\<SourceName\>/Type = "Beam" # Beam, Isotropic, Emittance or PhaseSpace
    s:So/\<SourceName\>/Component = "BeamPosition"
    i:So/\<SourceName\>/NumberOfHistoriesInRun = 0
    i:So/\<SourceName\>/NumberOfHistoriesInRandomJob = 0



Particle Source Parameters Used by Source Type Beam
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    s:So/\<SourceName\>/BeamParticle = "proton"
    d:So/\<SourceName\>/BeamEnergy = 169.23 MeV
    u:So/\<SourceName\>/BeamEnergySpread = 0.757504
    s:So/\<SourceName\>/BeamPositionDistribution = "Gaussian" # Flat or Gaussian
    s:So/\<SourceName\>/BeamPositionCutoffShape = "Ellipse" # Point, Ellipse, Rectangle or Isotropic
    d:So/\<SourceName\>/BeamPositionCutoffX = 10. cm
    d:So/\<SourceName\>/BeamPositionCutoffY = 10. cm
    d:So/\<SourceName\>/BeamPositionSpreadX = 0.65 cm
    d:So/\<SourceName\>/BeamPositionSpreadY = 0.65 cm
    s:So/\<SourceName\>/BeamAngularDistribution = "Gaussian" # Flat or Gaussian
    d:So/\<SourceName\>/BeamAngularCutoffX = 90. deg
    d:So/\<SourceName\>/BeamAngularCutoffY = 90. deg
    d:So/\<SourceName\>/BeamAngularSpreadX = 0.0032 rad
    d:So/\<SourceName\>/BeamAngularSpreadY = 0.0032 rad
 


Particle Source Parameters Used by Source Type Isotropic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    s:So/\<SourceName\>/and so on



Scoring Overall Control
~~~~~~~~~~~~~~~~~~~~~~~

::

    b:Sc/AddUnitEvenIfItIsOne = "False" # If unit is 1, rather than, say, Gy, default is to leave out unit in header.
    s:Sc/RootFileName = "topas" # name for root output files
    s:Sc/XmlFileName = "topas" # name for xml output files


Scoring Parameters Used by All Scorers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    s:Sc/\<ScorerName\>/Quantity = "DoseToMedium"


Scoring Parameters Used by All Volume Scorers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    s:Sc/\<ScorerName\>/Component = "Phantom"


Scoring Parameters Used by Scorer of Quantity DoseToMaterial
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    s:Sc/\<ScorerName\>/Material = "SomeMaterial"
    s:Sc/\<ScorerName\>/PreCalculateStoppingPowerRatios = "True" # defaults to "False"
    s:Sc/\<ScorerName\>/ProtonEnergyBinSize # default is 1 MeV
    s:Sc/\<ScorerName\>/MinProtonEnergyForStoppingPowerRatio # default is 1 MeV
    s:Sc/\<ScorerName\>/MaxProtonEnergyForStoppingPowerRatio # default is 500 MeV
    s:Sc/\<ScorerName\>/ElectronEnergyBinSize # default is 1 keV
    s:Sc/\<ScorerName\>/MinElectronEnergyForStoppingPowerRatio # default is 1 keV
    s:Sc/\<ScorerName\>/MaxElectronEnergyForStoppingPowerRatio # default is 1 MeV


Scoring Parameters Used by All Surface Scorers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    etc


Graphics Overall Control
~~~~~~~~~~~~~~~~~~~~~~~~

::

    b:Gr/Enable = "True" # Set False to avoid instantiating any part of Geant4 visualization system
    i:Gr/Verbosity = 0 # Set to higher integer to increase verbosity of Geant4 visualization system
    s:Gr/RefreshEvery = "Run" # "History", "Run" or "Session"
    i:Gr/ShowOnlyOutlineIfVoxelCountExceeds = 8000 # Above this limit, only show outer box
    i:Gr/SwitchOGLtoOGLIifVoxelCountExceeds = 70000000 # Above this limit, switch OpenGL Graphics to Immediate mode



Physics
~~~~~~~

::

    s:Ph/ListName = "Default"
    b:Ph/ListProcesses = "False" # Set true to dump list of active physics processes to console
    s:Ph/Default/Type = "Geant4_Modular"
    sv:Ph/Default/Modules = 6 "g4em-standard_opt4" "g4h-phy_QGSP_BIC_HP" "g4decay" "g4ion-binarycascade" "g4h-elastic_HP" "g4stopping"
    d:Ph/Default/EMRangeMin = 100. eV
    d:Ph/Default/EMRangeMax = 500. MeV



.. _parameters_default_elements:

Elements
~~~~~~~~

::

    s:El/Hydrogen/Symbol = "H"
    s:El/Helium/Symbol = "He"
    s:El/Lithium/Symbol = "Li"
    s:El/Beryllium/Symbol = "Be"
    s:El/Boron/Symbol = "B"
    s:El/Carbon/Symbol = "C"
    s:El/Nitrogen/Symbol = "N"
    s:El/Oxygen/Symbol = "O"
    s:El/Fluorine/Symbol = "F"
    s:El/Neon/Symbol = "Ne"
    s:El/Sodium/Symbol = "Na"
    s:El/Magnesium/Symbol = "Mg"
    s:El/Aluminum/Symbol = "Al"
    s:El/Silicon/Symbol = "Si"
    s:El/Phosphorus/Symbol = "P"
    s:El/Sulfur/Symbol = "S"
    s:El/Chlorine/Symbol = "Cl"
    s:El/Argon/Symbol = "Ar"
    s:El/Potassium/Symbol = "K"
    s:El/Calcium/Symbol = "Ca"
    s:El/Scandium/Symbol = "Sc"
    s:El/Titanium/Symbol = "Ti"
    s:El/Vanadium/Symbol = "V"
    s:El/Chromium/Symbol = "Cr"
    s:El/Manganese/Symbol = "Mn"
    s:El/Iron/Symbol = "Fe"
    s:El/Cobalt/Symbol = "Co"
    s:El/Nickel/Symbol = "Ni"
    s:El/Copper/Symbol = "Cu"
    s:El/Zinc/Symbol = "Zn"
    s:El/Gallium/Symbol = "Ga"
    s:El/Germanium/Symbol = "Ge"
    s:El/Arsenic/Symbol = "As"
    s:El/Selenium/Symbol = "Se"
    s:El/Bromine/Symbol = "Br"
    s:El/Krypton/Symbol = "Kr"
    s:El/Rubidium/Symbol = "Rb"
    s:El/Strontium/Symbol = "Sr"
    s:El/Yttrium/Symbol = "Y"
    s:El/Zirconium/Symbol = "Zr"
    s:El/Niobium/Symbol = "Nb"
    s:El/Molybdenum/Symbol = "Mo"
    s:El/Technetium/Symbol = "Tc"
    s:El/Ruthenium/Symbol = "Ru"
    s:El/Rhodium/Symbol = "Rh"
    s:El/Palladium/Symbol = "Pd"
    s:El/Silver/Symbol = "Ag"
    s:El/Cadmium/Symbol = "Cd"
    s:El/Indium/Symbol = "In"
    s:El/Tin/Symbol = "Sn"
    s:El/Antimony/Symbol = "Sb"
    s:El/Tellurium/Symbol = "Te"
    s:El/Iodine/Symbol = "I"
    s:El/Xenon/Symbol = "Xe"
    s:El/Caesium/Symbol = "Cs"
    s:El/Barium/Symbol = "Ba"
    s:El/Lanthanum/Symbol = "La"
    s:El/Cerium/Symbol = "Ce"
    s:El/Praseodymium/Symbol = "Pr"
    s:El/Neodymium/Symbol = "Nd"
    s:El/Promethium/Symbol = "Pm"
    s:El/Samarium/Symbol = "Sm"
    s:El/Europium/Symbol = "Eu"
    s:El/Gadolinium/Symbol = "Gd"
    s:El/Terbium/Symbol = "Tb"
    s:El/Dysprosium/Symbol = "Dy"
    s:El/Holmium/Symbol = "Ho"
    s:El/Erbium/Symbol = "Er"
    s:El/Thulium/Symbol = "Tm"
    s:El/Ytterbium/Symbol = "Yb"
    s:El/Lutetium/Symbol = "Lu"
    s:El/Hafnium/Symbol = "Hf"
    s:El/Tantalum/Symbol = "Ta"
    s:El/Tungsten/Symbol = "W"
    s:El/Rhenium/Symbol = "Re"
    s:El/Osmium/Symbol = "Os"
    s:El/Iridium/Symbol = "Ir"
    s:El/Platinum/Symbol = "Pt"
    s:El/Gold/Symbol = "Au"
    s:El/Mercury/Symbol = "Hg"
    s:El/Thallium/Symbol = "Tl"
    s:El/Lead/Symbol = "Pb"
    s:El/Bismuth/Symbol = "Bi"
    s:El/Polonium/Symbol = "Po"
    s:El/Astatine/Symbol = "At"
    s:El/Radon/Symbol = "Rn"
    s:El/Francium/Symbol = "Fr"
    s:El/Radium/Symbol = "Ra"



.. _parameters_default_materials:

Materials
~~~~~~~~~

::

    s:Ma/DefaultColor = "white"
    i:Ma/Verbosity = 0 # Set to 1 to report each time a material is defined

    sv:Ma/Vacuum/Components = 4 "Carbon" "Nitrogen" "Oxygen" "Argon"
    uv:Ma/Vacuum/Fractions = 4 0.000124 0.755268 0.231781 0.012827
    d:Ma/Vacuum/Density = 1.0E-25 g/cm3
    s:Ma/Vacuum/State = "Gas"
    d:Ma/Vacuum/Temperature = 2.73 kelvin
    d:Ma/Vacuum/Pressure = 3.0E-18 pascal
    s:Ma/Vacuum/DefaultColor = "skyblue"

    sv:Ma/Carbon/Components = 1 "Carbon"
    uv:Ma/Carbon/Fractions = 1 1.0
    d:Ma/Carbon/Density = 1.867 g/cm3
    d:Ma/Carbon/MeanExcitationEnergy = 78 eV
    s:Ma/Carbon/DefaultColor = "green"

    sv:Ma/Aluminum/Components = 1 "Aluminum"
    uv:Ma/Aluminum/Fractions = 1 1.0
    d:Ma/Aluminum/Density = 2.6989 g/cm3
    s:Ma/Aluminum/DefaultColor = "skyblue"
    i:Ma/Aluminum/AtomicNumber =  13
    d:Ma/Aluminum/AtomicMass = 26.98154 g/mole

    sv:Ma/Nickel/Components = 1 "Nickel"
    uv:Ma/Nickel/Fractions = 1 1.0
    d:Ma/Nickel/Density = 8.902 g/cm3
    s:Ma/Nickel/DefaultColor = "indigo"

    sv:Ma/Copper/Components = 1 "Copper"
    uv:Ma/Copper/Fractions = 1 1.0
    d:Ma/Copper/Density = 8.96 g/cm3
    s:Ma/Copper/DefaultColor = "orange"

    sv:Ma/Iron/Components = 1 "Iron"
    uv:Ma/Iron/Fractions = 1 1.0
    d:Ma/Iron/Density = 7.87 g/cm3
    s:Ma/Iron/DefaultColor = "skyblue"

    sv:Ma/Tantalum/Components = 1 "Tantalum"
    uv:Ma/Tantalum/Fractions = 1 1.0
    d:Ma/Tantalum/Density = 16.654 g/cm3
    s:Ma/Tantalum/DefaultColor = "indigo"

    sv:Ma/Lead/Components = 1 "Lead"
    uv:Ma/Lead/Fractions = 1 1.0
    d:Ma/Lead/Density = 11.35 g/cm3
    i:Ma/Lead/AtomicNumber =  82
    d:Ma/Lead/AtomicMass = 207.19 g/mole
    d:Ma/Lead/MeanExcitationEnergy = 823 eV
    s:Ma/Lead/DefaultColor = "brown"

    sv:Ma/Air/Components = 4 "Carbon" "Nitrogen" "Oxygen" "Argon"
    uv:Ma/Air/Fractions = 4 0.000124 0.755268 0.231781 0.012827
    d:Ma/Air/Density = 1.20484 mg/cm3
    d:Ma/Air/MeanExcitationEnergy = 85.7 eV
    s:Ma/Air/DefaultColor = "lightblue"

    sv:Ma/Brass/Components = 2 "Copper" "Zinc"
    uv:Ma/Brass/Fractions = 2 0.7 0.3
    d:Ma/Brass/Density = 8.550 g/cm3
    d:Ma/Brass/MeanExcitationEnergy = 324.4 eV
    s:Ma/Brass/DefaultColor = "grass"

    sv:Ma/Lexan/Components = 3 "Hydrogen" "Carbon" "Oxygen"
    uv:Ma/Lexan/Fractions = 3 0.055491 0.755751 0.188758
    d:Ma/Lexan/Density = 1.2 g/cm3
    d:Ma/Lexan/MeanExcitationEnergy = 73.1 eV
    s:Ma/Lexan/DefaultColor = "grey"

    sv:Ma/Lucite/Components = 3 "Hydrogen" "Carbon" "Oxygen"
    uv:Ma/Lucite/Fractions = 3 0.080538 0.599848 0.319614
    d:Ma/Lucite/Density = 1.190 g/cm3
    d:Ma/Lucite/MeanExcitationEnergy = 74.0 eV
    s:Ma/Lucite/DefaultColor = "grey"

    sv:Ma/Mylar/Components = 3 "Hydrogen" "Carbon" "Oxygen"
    uv:Ma/Mylar/Fractions = 3 0.041959 0.625017 0.333025
    d:Ma/Mylar/Density = 1.40 g/cm3
    s:Ma/Mylar/DefaultColor = "red"

    sv:Ma/Mylon/Components = 4 "Hydrogen" "Carbon" "Nitrogen" "Oxygen"
    uv:Ma/Mylon/Fractions = 4 0.097976 0.636856 0.123779 0.141389
    d:Ma/Mylon/Density = 1.140 g/cm3
    s:Ma/Mylon/DefaultColor = "purple"

    sv:Ma/Kapton/Components = 4 "Hydrogen" "Carbon" "Nitrogen" "Oxygen"
    uv:Ma/Kapton/Fractions = 4 0.026362 0.691133 0.073270 0.209235
    d:Ma/Kapton/Density = 1.420 g/cm3
    s:Ma/Kapton/DefaultColor = "purple"

    sv:Ma/Water_75eV/Components = 2 "Hydrogen" "Oxygen"
    uv:Ma/Water_75eV/Fractions = 2 0.111894 0.888106
    d:Ma/Water_75eV/Density = 1.0 g/cm3
    d:Ma/Water_75eV/MeanExcitationEnergy = 75.0 eV
    s:Ma/Water_75eV/DefaultColor = "blue"

    sv:Ma/Titanium/Components = 1 "Titanium"
    uv:Ma/Titanium/Fractions = 1 1.0
    d:Ma/Titanium/Density = 4.54 g/cm3
    s:Ma/Titanium/DefaultColor = "blue"

    sv:Ma/Steel/Components = 8 "Carbon" "Silicon" "Phosphorus" "Sulfur" "Chromium" "Manganese" "Iron" "Nickel"
    uv:Ma/Steel/Fractions = 8 0.0015 0.01 0.00045 0.0003 0.19 0.02 0.67775 0.1
    d:Ma/Steel/Density = 8.027 g/cm3
    s:Ma/Steel/DefaultColor = "lightblue"



Colors
~~~~~~

::

    iv:Gr/Color/White =     3 255 255 255
    iv:Gr/Color/Silver =    3 191 191 191
    iv:Gr/Color/Gray =	    3 127 127 127
    iv:Gr/Color/Grey =	    3 127 127 127
    iv:Gr/Color/Black =     3   0   0   0
    iv:Gr/Color/Red =       3 255   0   0
    iv:Gr/Color/Maroon =    3 127   0   0
    iv:Gr/Color/Yellow =    3 255 255   0
    iv:Gr/Color/Olive =     3 127 127   0
    iv:Gr/Color/Lime =      3   0 255   0
    iv:Gr/Color/Green =     3   0 127   0
    iv:Gr/Color/Aqua =      3   0 255 255
    iv:Gr/Color/Teal =      3   0 127 127
    iv:Gr/Color/Blue =	    3   0   0 255
    iv:Gr/Color/Navy =	    3   0   0 127
    iv:Gr/Color/Fuchsia =   3 255   0 255
    iv:Gr/Color/Purple =    3 127   0 127

    iv:Gr/Color/Lightblue = 3 175 255 255
    iv:Gr/Color/Skyblue =   3 175 124 255
    iv:Gr/Color/Magenta =   3 255   0 255
    iv:Gr/Color/Violet =    3 224   0 255
    iv:Gr/Color/Pink =      3 255   0 222
    iv:Gr/Color/Indigo =    3   0   0 190
    iv:Gr/Color/Grass =     3   0 239   0
    iv:Gr/Color/Orange =    3 241 224   0
    iv:Gr/Color/Brown =     3 225 126  66
    
    iv:Gr/Color/grey020 =   3  20  20  20
    iv:Gr/Color/grey040 =   3  40  40  40
    iv:Gr/Color/grey060 =   3  60  60  60
    iv:Gr/Color/grey080 =   3  80  80  80
    iv:Gr/Color/grey100 =   3 100 100 100
    iv:Gr/Color/grey120 =   3 120 120 120
    iv:Gr/Color/grey140 =   3 140 140 140
    iv:Gr/Color/grey160 =   3 160 160 160
    iv:Gr/Color/grey180 =   3 180 180 180
    iv:Gr/Color/grey200 =   3 200 200 200
    iv:Gr/Color/grey220 =   3 220 220 220
    iv:Gr/Color/grey240 =   3 240 240 240
    


Overall Control
~~~~~~~~~~

::

    b:Sc/MyScorer/OutputAfterRun = "True" # set True to trigger output of scorer after this run
    i:Ts/NumberOfThreads = 4 # defaults to 1
    b:Ts/BufferThreadOutput = "True" # Causes console output to be show one thread at a time
    i:Ts/Seed = 1 # default is 1
    b:Ts/PauseBeforeInit = "True"
    b:Ts/PauseBeforeSequence = "True"
    b:Ts/PauseBeforeQuit = "True"
    b:Ts/DumpNonDefaultParameters = "False" # Like above but omits defaults
    sv:Ts/DumpParametersToSimpleFile = 2 "SomeParameter" "SomeOtherParameter" # Dumps the requested parameter types, names and values to a simple, human-readable file, TopasParameterDump_Run0.txt
    sv:Ts/DumpParametersToSemicolonSeparatedFile = 2 "SomeParameter" "SomeOtherParameter" # Dumps the requested parameter types, names and values to a semicolon separated file, TopasParameterDumpSSF_Run0.txt. This file is suitable for easy import into other applications
    i:Ts/ShowHistoryCountAtInterval = 1 # how often to print history count to the console # If set to 0, history count will never be printed
    b:Ts/ShowHistoryCountOnSingleLine = "False" # Make count reuse a single line of console
    i:Ts/TrackingVerbosity = 0 # Set to larger integer to see details of tracking
    b:Ts/ShowCPUTime = "True" # Show CPU time used in various phases of the simulation
    i:Ts/RunIDPadding = 4 # Run numbers are padded in output files, such as MyScoringOutput_Run_0001.csv, so that they will sort naturally in various file viewers. This parameter sets how many places of padding are used.
    Ge/MyComponent/Include = "False"
    Sc/MyScorer/Active = "False"
    Gr/MyGraphics/Active = "False"
        


Materials
~~~~~~~~~~

::

    i:Ma/MyMaterial/VariableDensityBins = 100
    u:Ma/MyMaterial/VariableDensityMin = .1
    u:Ma/MyMaterial/VariableDensityMax = 10
    i:Is/U235/Z = 92
    i:Is/U235/N = 235
    d:Is/U235/A = 235.01 g/mole
    i:Is/U238/Z = 92
    i:Is/U238/N = 238
    d:Is/U238/A = 238.03 g/mole
    s:El/MyEIU/Symbol = "MyElU"
    sv:El/MyElU/IsotopeNames = 2 "U235" "U238"
    uv:El/MyElU/IsotopeAbundances = 2 90. 10
        


Particle Source
~~~~~~~~~~~~~~~~

::

    i:So/MySource/NumberOfHistoriesInRun = 100
    i:So/MySource/NumberOfHistoriesInRun = 10
    i:So/MySource/NumberOfHistoriesInRun = Tf/MyBCMTimeFeature/Value
    i:So/MySource/NumberOfHistoriesInRandomJob = 1000 # defaults to 100
    d:So/MySource/ProbabilityOfUsingAGivenRandomTime = Tf/MyBCMTimeFeature/Value
    So/MySource/NumberOfHistoriesInRun = 0
            


                


Placement of Components
~~~~~~~~~~~~~~~~~~~~~~~~

::

    s:Ge/MyBox/Type="TsBox"
    s:Ge/MyBox/Parent = "World"
    s:Ge/MyBox/Material="Air"
    d:Ge/MyBox/HLX=5. m # Half Length
    d:Ge/MyBox/HLY=5. m
    d:Ge/MyBox/HLZ=5. m
    d:Ge/MyBox/TransX=0. m
    d:Ge/MyBox/TransY=0. m
    d:Ge/MyBox/TransZ=0. m
    d:Ge/MyBox/RotX=0. deg
    d:Ge/MyBox/RotY=0. deg
    d:Ge/MyBox/RotZ=0. deg
    
    # Overrides the world size that was set in built-in defaults:
    Ge/World/HLX=10. m
    Ge/World/HLY=10. m
    Ge/World/HLZ=10. m

    # Box inserted into the World
    s:Ge/TestBox/Material="Air"
    s:Ge/TestBox/Parent="World"
    s:Ge/TestBox/Type="TsBox"
    d:Ge/TestBox/HLX=400. cm
    d:Ge/TestBox/HLY=300. cm
    d:Ge/TestBox/HLZ=200. cm
    d:Ge/TestBox/TransX=0. m
    d:Ge/TestBox/TransY=0. cm
    d:Ge/TestBox/TransZ=0. m
    d:Ge/TestBox/RotX=0. deg
    d:Ge/TestBox/RotY=0. deg
    d:Ge/TestBox/RotZ=0. deg

    # Another box inserted into the first box
    s:Ge/TestBox2/Material="Carbon"
    s:Ge/TestBox2/Parent="TestBox"
    s:Ge/TestBox2/Type="TsBox"
    d:Ge/TestBox2/HLX=180. cm
    d:Ge/TestBox2/HLY=120. cm
    d:Ge/TestBox2/HLZ=80. cm
    d:Ge/TestBox2/TransX=0. m
    d:Ge/TestBox2/TransY=0. cm
    d:Ge/TestBox2/TransZ=150. cm
    d:Ge/TestBox2/RotX=0. deg
    d:Ge/TestBox2/RotY=30. deg
    d:Ge/TestBox2/RotZ=0. deg
    Ge/CheckForOverlaps = "False"
    b:Ge/CheckInsideEnvelopesForOverlaps = "True"
    i:Ge/CheckForOverlapsResolution = 1000
    d:Ge/CheckForOverlapsTolerance = 0. mm
    d:Ge/Gantry1/Scatterer2/RotZForSS0 = 0. deg
    d:Ge/Gantry1/Scatterer2/RotZForSS8 = 270. deg
    d:Ge/Gantry1/Scatterer2/RotZForSS2 = 180. deg
    d:Ge/Gantry1/Scatterer2/RotZForSS3 = 90. deg
    Ge/Scatterer2/Holder/RotZ = Ge/Gantry1/Scatterer2/RotZForSS3 deg
                


Range Modulator Wheel
~~~~~~~~~~~~~~~~~~~~~~

::

    # Common parameters: type of geometry, position, and rotation
    s:Ge/RangeModulatorA/Type = "TsRangeModulator"
    s:Ge/RangeModulatorA/Material = "Parent"
    s:Ge/RangeModulatorA/Parent = "World"
    d:Ge/RangeModulatorA/TransX = 10.0 cm
    d:Ge/RangeModulatorA/TransY = 0.0 cm
    d:Ge/RangeModulatorA/TransZ = 0.0 cm
    d:Ge/RangeModulatorA/RotX = 0.0 deg
    d:Ge/RangeModulatorA/RotY = 0.0 deg
    d:Ge/RangeModulatorA/RotZ = 0.0 deg
    b:Ge/RangeModulatorA/Invisible = "TRUE"

    # Set height of each sections and total height = 160.0 mm
    d:Ge/RangeModulatorA/HeightOfUpper = 150 mm
    d:Ge/RangeModulatorA/HeightOfMiddle = 1.0 mm
    d:Ge/RangeModulatorA/HeightOfLower = 9.0 mm

    # Shell dimensions, material, color, etc.
    d:Ge/RangeModulatorA/Shell/Rin = 15.0 cm
    d:Ge/RangeModulatorA/Shell/Rout = 15.5 cm
    s:Ge/RangeModulatorA/Shell/Material = "Aluminum"
    s:Ge/RangeModulatorA/Shell/Color = "grey"
    s:Ge/RangeModulatorA/Shell/DrawingStyle = "Solid"
    i:Ge/RangeModulatorA/Shell/VisSegsPerCircle = 360

    # Hub dimensions, material, color, etc.
    d:Ge/RangeModulatorA/Hub/Rin = 6.0 cm
    d:Ge/RangeModulatorA/Hub/Rout = 7.0 cm
    s:Ge/RangeModulatorA/Hub/Material = "Aluminum"
    s:Ge/RangeModulatorA/Hub/Color = "grey"
    s:Ge/RangeModulatorA/Hub/DrawingStyle = "Solid"
    i:Ge/RangeModulatorA/Hub/VisSegsPerCircle = 360

    # Setting tracks on Upper area
    # Two tracks Track1 (7.0 cm ~ 11.0 cm) and Track2 ( 11.0 cm ~ 15.0 cm)
    dv:Ge/RangeModulatorA/Upper/RadialDivisions=1 11.0 cm

    # Assignment of track pattern of Upper area
    # Track1 refers the pattern named "LexanBlockT1" whose vector parameters are defined elsewhere (see below).
    s:Ge/RangeModulatorA/Upper/Track1/Pattern = "LexanBlockT1"
    s:Ge/RangeModulatorA/Upper/Track2/Pattern = "NULL" #NULL means empty track.

    # Track1 pattern: 14 blocks of Lexan.
    # Numbers of Angles, Heights, and Materials should be same.
    d:Ge/LexanBlockT1/Offset=0.0 deg #means shift of zero-angle
    # Angle divisions. The first block’s spans from 5.0 deg to 115.0 deg.
    # The last block starting at 324.0 deg spans to the first block’s boundary.
    # This case last block spans from 324.0 deg to 360.0 + 5.0 deg
    dv:Ge/LexanBlockT1/Angles=14
    5.00 115.00 146.50 173.2 195.07
    216.15 230.14 243.00 255.5 270.60
    282.20 294.60 306.20 324.00 deg
    # Height of each block.
    # Note that zero height means that no block in that angle range.
    dv:Ge/LexanBlockT1/Heights=14
    77.0 82.0 87.0 92.15 95.0
    100.4 106.0 110.2 115.3 119.5
    124.0 128.8 132.00 60.0 mm

    # Material of each block.
    sv:Ge/LexanBlockT1/Materials=14
    "Lexan" "Lexan" "Lexan" "Lexan" "Lexan"
    "Lexan" "Lexan" "Lexan" "Lexan" "Lexan"
    "Lexan" "Lexan" "Lexan" "Brass"
    
    b:Ge/RangeModulatorA/PrintInformation = "True" #Print out specification, see below
    
    
