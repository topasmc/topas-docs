.. _parameters_default:

Index To Parameters
==================

This index is intended to list all of the parameters used by TOPAS (though we may have missed a few).
When we get some more time to work on this, we will make each parameter be a link to relevant part of the TOPAS User Guide, but that part of the work is not done yet.



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
    s:Tf/<TimeFeatureName>/Function = "Step"
    sv:Tf/<TimeFeatureName>/Values = 3 "image1" "image2" "image3"



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

    s:Ge/<ComponentName>/Type = "TsBox"
    s:Ge/<ComponentName/Parent = "World"
    s:Ge/<ComponentName>/Material = "Air"
    d:Ge/<ComponentName>/TransX = 0. m
    d:Ge/<ComponentName>/TransY = 0. m
    d:Ge/<ComponentName>/TransZ = 0. m
    d:Ge/<ComponentName>/RotX = 0. deg
    d:Ge/<ComponentName>/RotY = 0. deg
    d:Ge/<ComponentName>/RotZ = 0. deg
    b:Ge/<ComponentName/Include = "False" # defaults to "True"
    d:Ge/<ComponentName/MaxStepSize = 1. mm # sets maximum step size used in this component
    i:Ge/<ComponentName>/CheckForOverlapsResolution = 1000
    d:Ge/<ComponentName>/CheckForOverlapsTolerance = 0. mm
    b:Ge/<ComponentName>/IsParallel = "True"
    s:Ge/<ComponentName>/ParallelWorldName = "SomeParallelWorldName"
    s:Ge/<ComponentName>/Field = "DipoleMagnet" # "DipoleMagnet", "QuadrupoleMagnet", "MappedMagnet", "UniformElectroMagnetic" or your own definition
    u:Ge/<ComponentName>/MagneticFieldDirectionX = 0.0
    u:Ge/<ComponentName>/MagneticFieldDirectionY = 1.0
    u:Ge/<ComponentName>/MagneticFieldDirectionZ = 0.0
    d:Ge/<ComponentName>/MagneticFieldStrength = 3.0 tesla
    d:Ge/<ComponentName>/MagneticFieldGradientX = 1.0 tesla
    d:Ge/<ComponentName>/MagneticFieldGradientY = 1.0 tesla
    s:Ge/<ComponentName>/MagneticField3DTable = "PurgMag3D.TABLE"
    u:Ge/<ComponentName>/ElectricFieldDirectionX = 1.0
    u:Ge/<ComponentName>/ElectricFieldDirectionY = 1.0
    u:Ge/<ComponentName>/ElectricFieldDirectionZ = 0.0
    d:Ge/<ComponentName>/ElectricFieldStrength   = 5000 kV/cm
    u:Ge/<ComponentName>/MagneticFieldDirectionX = 0.0
    u:Ge/<ComponentName>/MagneticFieldDirectionY = 1.0
    u:Ge/<ComponentName>/MagneticFieldDirectionZ = 0.0
    d:Ge/<ComponentName>/MagneticFieldStrength   = 5.0 tesla
    d:Ge/<ComponentName>/MagneticFieldStrength = Tf/BField1st/Value tesla
    s:Ge/<ComponentName>/FieldStepper = "ClassicalRK4"
    d:Ge/<ComponentName>/FieldStepMinimum = 1.0 mm
    d:Ge/<ComponentName>/FieldDeltaChord = 1.0e-1 mm
    d:Ge/<ComponentName>/Scatterer2/RotZForSS0 = 0. deg
    d:Ge/<ComponentName>/Scatterer2/RotZForSS8 = 270. deg
    d:Ge/<ComponentName>/Scatterer2/RotZForSS2 = 180. deg
    d:Ge/<ComponentName>/Scatterer2/RotZForSS3 = 90. deg
    Ge/<ComponentName>/Holder/RotZ = Ge/Gantry1/Scatterer2/RotZForSS3 deg
    s:Ge/<ComponentName>/Color = "red"
    s:Ge/<ComponentName>/DrawingStyle = "Solid" # "Solid", "Wireframe" or "FullWireFrame"
    i:Ge/<ComponentName>/VisSegsPerCircle = 100 # Number of line segments to use to approximate a circle, defaults to 24
    sv:Ge/<ComponentName>/VoxelMaterials = 100 "G4_WATER" "G4_WATER" "Air" "Air" "G4_WATER" ...
    s:Ge/<ComponentName>/InputFile = "Foot" # file name, without extensions. Match exact case
    s:Ge/<ComponentName>/FileFormat = "ply" # file extension
    b:Ge/<ComponentName>/PrintPoints = "True"
    s:Ge/<ComponenName>/AssignToRegionNamed = "MyRegion"
    s:Ge/<ComponenName>/OpticalBehaviorTo/MyComponent2 = "MySurface1"
    s:Ge/<ComponenName>/OpticalBehaviorTo/MyComponent1 = "MySurface2"
    s:Ge/<ComponenName>/OpticalBehavior = "MySurface1"
    s:Ge/<ComponentName>/Water/UpstreamSurface = Ge/WaterTank/Water/ZMinusSurface



Geometry Parameters for Component Type TsBox
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    d:Ge/<ComponentName>/HLX = 5. m # Half Length
    d:Ge/<ComponentName>/HLY = 5. m
    d:Ge/<ComponentName>/HLZ = 5. m
    b:Ge/<ComponentName>/Invisible = "TRUE"



Geometry Parameters for Component Type TsSphere
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    d:Ge/<ComponentName>/RMax = 5. m
    d:Ge/<ComponentName>/RMin = 0. m
    d:Ge/<ComponentName>/DPhi = 0. deg
    d:Ge/<ComponentName>/SPhi = 180. deg



Geometry Parameters for Component Type Range Modulator Wheel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    d:Ge/<ComponentName>/HeightOfUpper = 150 mm
    d:Ge/<ComponentsName>/HeightOfMiddle = 1.0 mm
    d:Ge/<ComponentName>/HeightOfLower = 9.0 mm
    d:Ge/<ComponentName>/Shell/Rin = 15.0 cm
    d:Ge/<ComponentName>/Shell/Rout = 15.5 cm
    s:Ge/<ComponentName>/Shell/Material = "Aluminum"
    s:Ge/<ComponentName>/Shell/Color = "grey"
    s:Ge/<ComponentName>/Shell/DrawingStyle = "Solid"
    i:Ge/<ComponentName>/Shell/VisSegsPerCircle = 360
    d:Ge/<ComponentName>/Hub/Rin = 6.0 cm
    d:Ge/<ComponentName>/Hub/Rout = 7.0 cm
    s:Ge/<ComponentName>/Hub/Material = "Aluminum"
    s:Ge/<ComponentName>/Hub/Color = "grey"
    s:Ge/<ComponentName>/Hub/DrawingStyle = "Solid"
    i:Ge/<ComponentName>/Hub/VisSegsPerCircle = 360
    dv:Ge/<ComponentName>/Upper/RadialDivisions=1 11.0 cm
    s:Ge/<ComponentName>/Upper/Track1/Pattern = "LexanBlockT1"
    s:Ge/<ComponentName>/Upper/Track2/Pattern = "NULL" #NULL means empty track.
    b:Ge/<ComponentName>/PrintInformation = "True" #Print out specification, see below

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
    


Geometry Parameters for Component Type Propeller
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    i:Ge/<ComponentName>/NbOfBlades = 4 #Number of blades
    dv:Ge/<ComponentName>/Thickness =1 0.356 mm #thickness
    


Geometry Parameters for Component Type Ridge Filter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    dv:Ge/<ComponentName>/XPoints = 8
    dv:Ge/<ComponentName>/ZPoints = 8
    dv:Ge/<ComponentName>/Displacement = 3 -5.0 0.0 5.0 mm
        


Geometry Parameters for Component Type Multi Wire Chamber
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    d:Ge/<ComponentName>/Layer2/PosZ=-5.0 cm
        


Geometry Parameters for Component Type Multi Leaf Collimator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    d:Ge/<ComponentName>/MaximumLeafOpen = 5.0 cm
    dv:Ge/<ComponentName>/XMinusLeavesOpen = 5 0.0 -0.3 -0.2 -0.5 0.0 cm
    dv:Ge/<ComponentName>/XPlusLeavesOpen = 5 0.0 0.3 0.2 0.5 0.0 cm
        


Geometry Parameters for Component Type CAD (Computer Aided Design)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    d:Ge/<ComponentName>/Units = 1.0 cm # how to interpret dimension numbers in the file. Changing this value will re-scale the component
        


Geometry Parameters for Component Type Compensator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    d:Ge/<ComponentName>/InvHL = -0.5 * Ge/Compensator/Thickness cm
    s:Ge/<ComponentName>/Method = "ExtrudedSolid" # Polyhedra, ExtrudedSolid, SubtractionCylinders or UnionCylinders
    d:Ge/<ComponentName>/XTolerance = 1. mm
    d:Ge/<ComponentName>/YTolerance = 1. mm
        


Geometry Parameters for Type Patient Components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    b:Ge/<ComponentName>/DumpImagingValues = "True"
    b:Ge/<ComponentName>/PreLoadAllMaterials = "True"
    s:Ge/<ComponentName>/DicomDirectory = "DICOM_Box"
    sv:Ge/<ComponentName>/DicomModalityTags = 1 "CT" # defaults to just CT
    sv:Ge/<ComponentName>/ColorByRTStructNames = 2 "R_LUNG" "L_LUNG"
    sv:Ge/<ComponentName>/ColorByRTStructColors = 2 "yellow" "red"
    b:Ge/<ComponentName>/FakeStructures = "True"
    dc:Ge/<ComponentName>/DicomOriginX = 0.0 mm
    dc:Ge/<ComponentName>/DicomOriginY = 0.0 mm
    dc:Ge/<ComponentName>/DicomOriginZ = 0.0 mm
    s:Ge/<ComponentName>/CloneRTDoseGridFrom
    dv:Ge/<ComponentName>/CloneRTDoseGridSize
    s:Ge/<ComponentName>/InputDirectory = "./"
    s:Ge/<ComponentName>/MetaDataFile = "XCAT_FullMouse_86x86x161_atn_1.log"
    s:Ge/<ComponentName>/DataType  = “FLOAT” # “SHORT”, “INT” or “FLOAT"
    i:Ge/<ComponentName>/NumberOfVoxelsX  = 86
    i:Ge/<ComponentName>/NumberOfVoxelsY  = 86
    i:Ge/<ComponentName>/NumberOfVoxelsZ = 161
    d:Ge/<ComponentName>/VoxelSizeX       = .5 mm
    d:Ge/<ComponentName>/VoxelSizeY       = .5 mm
    d:Ge/<ComponentName>/VoxelSizeZ       = .5 mm
    iv:Ge/<ComponentName>/NumberOfVoxelsZ = 2 10 20
    dv:Ge/<ComponentName>/VoxelSizeZ = 2 2.5 1.25 mm
    u:Ge/<ComponentName>/AttenuationForMaterial_XCAT_Air    =   0.
    u:Ge/<ComponentName>/AttenuationForMaterial_XCAT_Muscle = 195.2515
    u:Ge/<ComponentName>/AttenuationForMaterial_XCAT_Lung   =  57.5347
    s:Ge/<ComponentName>/ImagingToMaterialConverter = "XCAT_Attenuation" # "XCAT_Activity"
    u:Ge/<ComponentName>/AttenuationForMaterial_XCAT_Air    =   0.
    u:Ge/<ComponentName>/AttenuationForMaterial_XCAT_Muscle = 195.2515
    u:Ge/<ComponentName>/AttenuationForMaterial_XCAT_Lung   =  57.5347
    dv:Ge/<ComponentName>/DensityCorrection = 3996 9.35212 5.55269 4.14652 ...1.06255 1.00275 g/cm3
    iv:Ge/<ComponentName>/SchneiderHounsfieldUnitSections = 8 -1000 -98 15 23 101 2001 2995 2996
    uv:Ge/<ComponentName>/SchneiderDensityOffset = 7 0.00121 1.018 1.03 1.003 1.017 2.201 4.54
    uv:Ge/<ComponentName>/SchneiderDensityFactor = 7 0.00103 0.00089 0.0 0.00117 0.00059 0.0005 0.0
    uv:Ge/<ComponentName>/SchneiderDensityFactorOffset = 7 1000. 0. 1000. 0. 0. -2000. 0
    iv:Ge/<ComponentName>/SchneiderHUToMaterialSections = 26 -1000 -950 -120 -83 ... 1500 2995 2996
    sv:Ge/<ComponentName>/SchneiderElements = 13 "Hydrogen" "Carbon" "Nitrogen" "Oxygen" 
    uv:Ge/<ComponentName>/SchneiderMaterialsWeight1 = 13 0.0   0.0   0.755 0.232 
    uv:Ge/<ComponentName>/SchneiderMaterialsWeight2 = 13 0.103 0.105 0.031 0.749 
    dv:Ge/<ComponentName>/SchneiderMaterialMeanExcitationEnergy = 26 88.8 0. 77.7. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. eV





Particle Source Parameters Used by All Source Types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    s:So/<SourceName>/Type = "Beam" # Beam, Isotropic, Emittance or PhaseSpace
    s:So/<SourceName>/Component = "BeamPosition"
    i:So/<SourceName>/NumberOfHistoriesInRun = 0
    i:So/<SourceName>/NumberOfHistoriesInRandomJob = 0



Particle Source Parameters Used by Source Type Beam
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    s:So/<SourceName>/BeamParticle = "proton"
    d:So/<SourceName>/BeamEnergy = 169.23 MeV
    u:So/<SourceName>/BeamEnergySpread = 0.757504
    s:So/<SourceName>/BeamPositionDistribution = "Gaussian" # Flat or Gaussian
    s:So/<SourceName>/BeamPositionCutoffShape = "Ellipse" # Point, Ellipse, Rectangle or Isotropic
    d:So/<SourceName>/BeamPositionCutoffX = 10. cm
    d:So/<SourceName>/BeamPositionCutoffY = 10. cm
    d:So/<SourceName>/BeamPositionSpreadX = 0.65 cm
    d:So/<SourceName>/BeamPositionSpreadY = 0.65 cm
    s:So/<SourceName>/BeamAngularDistribution = "Gaussian" # Flat or Gaussian
    d:So/<SourceName>/BeamAngularCutoffX = 90. deg
    d:So/<SourceName>/BeamAngularCutoffY = 90. deg
    d:So/<SourceName>/BeamAngularSpreadX = 0.0032 rad
    d:So/<SourceName>/BeamAngularSpreadY = 0.0032 rad
 


Particle Source Parameters Used by Source Type Emmittance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    s:So/<SourceName>/Distribution = "BiGaussian" # distribution name
    d:So/<SourceName>/SigmaX = 0.2 mm # std of x positions
    u:So/<SourceName>/SigmaXprime = 0.032 # std of x’, note that it’s unitless. 1 equals to 1.0 rad.
    u:So/<SourceName>/CorrelationX = -0.9411 # correlation of x and x’
    d:So/<SourceName>/SigmaY = 0.2 mm # std of y positions
    u:So/<SourceName>/SigmaYPrime = 0.032 # std of y’
    u:So/<SourceName>/CorrelationY = 0.9411 # correlation of y and y’
    u:So/<SourceName>/AlphaX = 0.2
    d:So/<SourceName>/BetaX  = 600.0 mm
    d:So/<SourceName>/EmittanceX = 0.01 mm # we don’t multiply pi intrinsically.
    u:So/<SourceName>/AlphaY = 2.5
    d:So/<SourceName>/BetaY = 1400.0 mm
    d:So/<SourceName>/EmittanceY = 0.02 mm
    u:So/<SourceName>/ParticleFractionX = 0.90
    u:So/<SourceName>/ParticleFractionY = 0.90



Particle Source Parameters Used by Source Type Phase Space
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    b:So/<SourceName>/LimitedAssumePhotonIsNewHistory = "true"
    s:So/<SourceName>/PhaseSpaceFileName = "ASCIIOutput" # match exact case
    s:So/<SourceName>/PhaseSpaceIncludeEmptyHistories = "False" # defaults to false
    s:So/<SourceName>/PhaseSpacePreCheck = "True" # defaults to true
    u:So/<SourceName>/PhaseSpaceScaleXPosBy = 0.1 # adjust starting point on X axis by factor of 0.1
    u:So/<SourceName>/PhaseSpaceScaleYPosBy = 0.1 # adjust starting point on Y axis by factor of 0.1
    u:So/<SourceName>/PhaseSpaceScaleZPosBy = 0.1 # adjust starting point on Z axis by factor of 0.1
    b:So/<SourceName>/PhaseSpaceInvertXAxis = "True"
    b:So/<SourceName>/PhaseSpaceInvertYAxis = "True"
    b:So/<SourceName>/PhaseSpaceInvertZAxis = "True"
    i:So/<SourceName>/PhaseSpaceMultipleUse = 2 # reuse this phase space multiple times
    i:So/<SourceName>/PhaseSpaceBufferSize = 1000000
    s:So/<SourceName>/PhaseSpaceIncludeEmptyHistories = "True"



Particle Source Parameters Used by Source Type Miscellaneous
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    i:So/<SourceName>/NumberOfHistoriesInRandomJob = 100
    d:So/<SourceName>/ProbabilityOfUsingAGivenRandomTime = 1.
    sv:So/<SourceName>/OnlyIncludeParticlesCharged = 1 "Negative"
    sv:So/<SourceName>/OnlyIncludeParticlesNotCharged = 1 "Negative"
    i:So/<SourceName>/OnlyIncludeParticlesOfAtomicMass = 10 # allow all ions of atomic mass 10
    i:So/<SourceName>/OnlyIncludeParticlesNotOfAtomicMass = 10
    i:So/<SourceName>/OnlyIncludeParticlesOfAtomicNumber = 6 # allow all ions of Carbon
    i:So/<SourceName>/OnlyIncludeParticlesNotOfAtomicNumber = 6
    d:So/<SourceName>/OnlyIncludeParticlesWithInitialKEBelow = 1. MeV
    d:So/<SourceName>/OnlyIncludeParticlesWithInitialKENotBelow = 1. MeV
    d:So/<SourceName>/OnlyIncludeParticlesWithInitialKE = 1. MeV
    d:So/<SourceName>/OnlyIncludeParticlesWithInitialKENot = 1. MeV
    d:So/<SourceName>/OnlyIncludeParticlesWithInitialKEAbove = 10. MeV
    d:So/<SourceName>/OnlyIncludeParticlesWithInitialKENotAbove = 10. MeV
    d:So/<SourceName>/OnlyIncludeParticlesWithInitialMomentumBelow = 1. MeV
    d:So/<SourceName>/OnlyIncludeParticlesWithInitialMomentumNotBelow = 1. MeV
    d:So/<SourceName>/OnlyIncludeParticlesWithInitialMomentum = 1. MeV
    d:So/<SourceName>/OnlyIncludeParticlesWithInitialMomentumNot = 1. MeV
    d:So/<SourceName>/OnlyIncludeParticlesWithInitialMomentumAbove = 10. MeV
    d:So/<SourceName>/OnlyIncludeParticlesWithInitialMomentumNotAbove = 10. MeV
    sv:So/<SourceName>/OnlyIncludeParticlesNamed = 2 "proton" "neutron"
    sv:So/<SourceName>/OnlyIncludeParticlesNotNamed = 2 "proton" "neutron"
    sv:So/<SourceName>/OnlyIncludeParticlesNamed = 1 "proton"
    d:So/<SourceName>/OnlyIncludeParticlesWithInitialKEAbove = 100. MeV # minimum energy
    sv:So/<SourceName>/OnlyIncludeParticlesNamed = 2 "proton" "neutron"
    d:So/<SourceName>/OnlyIncludeParticlesWithInitialKEAbove = 100. MeV # minimum energy
    b:So/<SourceName>/InvertFilter = "True"



Scoring Overall Control
~~~~~~~~~~~~~~~~~~~~~~~

::

    b:Sc/AddUnitEvenIfItIsOne = "False" # If unit is 1, rather than, say, Gy, default is to leave out unit in header.
    s:Sc/RootFileName = "topas" # name for root output files
    s:Sc/XmlFileName = "topas" # name for xml output files
    i:Sc/<ScorrerName>/XBins = 512
    i:Sc/<ScorrerName>/YBins = 512
    i:Sc/<ScorrerName>/ZBins = 256


Scoring Parameters Used by All Scorers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    s:Sc/<ScorerName>/Quantity = "DoseToMedium"


Scoring Parameters Used by All Volume Scorers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    s:Sc/<ScorerName>/Component = "Phantom"
    


Scoring Parameters Used by Scorer of Quantity DoseToMaterial
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    s:Sc/<ScorerName>/Material = "SomeMaterial"
    s:Sc/<ScorerName>/PreCalculateStoppingPowerRatios = "True" # defaults to "False"
    s:Sc/<ScorerName>/ProtonEnergyBinSize # default is 1 MeV
    s:Sc/<ScorerName>/MinProtonEnergyForStoppingPowerRatio # default is 1 MeV
    s:Sc/<ScorerName>/MaxProtonEnergyForStoppingPowerRatio # default is 500 MeV
    s:Sc/<ScorerName>/ElectronEnergyBinSize # default is 1 keV
    s:Sc/<ScorerName>/MinElectronEnergyForStoppingPowerRatio # default is 1 keV
    s:Sc/<ScorerName>/MaxElectronEnergyForStoppingPowerRatio # default is 1 MeV
    


Scoring Parameters Used by Scorer of Quantity ProtonLET Scorer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    s:Sc/<ScorerName>/WeightBy = "Track" # defaults to "Dose"
    d:Sc/<ScorerName>/MaxScoredLET = 100 MeV/mm/(g/cm3) # default 100 MeV/mm/(g/cm3)
    b:Sc/<ScorerName>/UsePreStepLookup = "True" # defaults to “False”
    d:Sc/<ScorerName>/NeglectSecondariesBelowDensity = 0.1 g/cm3
    d:Sc/<ScorerName>/UseFluenceWeightedBelowDensity = 0. g/cm3



Scoring Parameters Used by All Surface Scorers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    s:Sc/<ScorerName>/Surface = "Phantom/ZMinusSurface"
    s:Sc/<ScorerName>/Surface = Ge/WaterTank/Water/UpstreamSurface
    


Scoring Parameters Used by All Phase Space Scorers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    s:Sc/<ScorerName>/OutputType = "ASCII" # "Binary", "ASCII," "Limited" or "ROOT"
    b:Sc/<ScorerName>/IncludeTOPASTime = "True" # Time used by TimeFeatures for this history
    b:Sc/<ScorerName>/IncludeTimeOfFlight = "True" # Time of Flight of this particle from start of history to scoring plane
    b:Sc/<ScorerName>/IncludeRunID = "True"
    b:Sc/<ScorerName>/IncludeEventID = "True"
    b:Sc/<ScorerName>/IncludeTrackID = "True"
    b:Sc/<ScorerName>/IncludeParentID = "True" # Track ID of parent particle
    b:Sc/<ScorerName>/IncludeCharge = "True"
    b:Sc/<ScorerName>/IncludeCreatorProcess = "True"
    b:Sc/<ScorerName>/IncludeVertexInfo = "True" # Initial KE, Position and Momentum
    b:Sc/<ScorerName>/IncludeSeed = "True"
    i:Sc/<ScorerName>/OutputBufferSize = 1000 # Number of particles in phase space buffer
   


Scoring Parameters Used by All Filtering Scorers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    s:Sc/<ScorerName>/OnlyIncludeParticlesOfGeneration = "Primary"
    sv:Sc/<ScorerName>/OnlyIncludeParticlesCharged = 1 "Negative"
    sv:Sc/<ScorerName>/OnlyIncludeParticlesNotCharged = 1 "Negative"
    i:Sc/<ScorerName>/OnlyIncludeParticlesOfAtomicMass = 10    # allow all ions of atomic mass 10
    i:Sc/<ScorerName>/OnlyIncludeParticlesNotOfAtomicMass = 10
    i:Sc/<ScorerName>/OnlyIncludeParticlesOfAtomicNumber = 6   # allow all ions of Carbon
    i:Sc/<ScorerName>/OnlyIncludeParticlesNotOfAtomicNumber = 6
    d:Sc/<ScorerName>/OnlyIncludeParticlesWithInitialKEBelow = 1. MeV
    d:Sc/<ScorerName>/OnlyIncludeParticlesWithInitialKENotBelow = 1. MeV
    d:Sc/<ScorerName>/OnlyIncludeParticlesWithInitialKE = 1. MeV
    d:Sc/<ScorerName>/OnlyIncludeParticlesWithInitialKENot = 1. MeV
    d:Sc/<ScorerName>/OnlyIncludeParticlesWithInitialKEAbove = 10. MeV
    d:Sc/<ScorerName>/OnlyIncludeParticlesWithInitialKENotAbove = 10. MeV
    d:Sc/<ScorerName>/OnlyIncludeParticlesWithInitialMomentumBelow = 1. MeV
    d:Sc/<ScorerName>/OnlyIncludeParticlesWithInitialMomentumNotBelow = 1. MeV
    d:Sc/<ScorerName>/OnlyIncludeParticlesWithInitialMomentum = 1. MeV
    d:Sc/<ScorerName>/OnlyIncludeParticlesWithInitialMomentumNot = 1. MeV
    d:Sc/<ScorerName>/OnlyIncludeParticlesWithInitialMomentumAbove = 10. MeV
    d:Sc/<ScorerName>/OnlyIncludeParticlesWithInitialMomentumNotAbove = 10. MeV
    d:Sc/<ScorerName>/OnlyIncludeIfIncidentParticleKEBelow = 1. MeV
    d:Sc/<ScorerName>/OnlyIncludeIfIncidentParticleKENotBelow = 1. MeV
    d:Sc/<ScorerName>/OnlyIncludeIfIncidentParticleKE = 1. MeV
    d:Sc/<ScorerName>/OnlyIncludeIfIncidentParticleKENot = 1. MeV
    d:Sc/<ScorerName>/OnlyIncludeIfIncidentParticleKEAbove = 10. MeV
    d:Sc/<ScorerName>/OnlyIncludeIfIncidentParticleKENotAbove = 10. MeV
    d:Sc/<ScorerName>/OnlyIncludeIfIncidentParticleMomentumBelow = 1. MeV
    d:Sc/<ScorerName>/OnlyIncludeIfIncidentParticleMomentumNotBelow = 1. MeV
    d:Sc/<ScorerName>/OnlyIncludeIfIncidentParticleMomentum = 1. MeV
    d:Sc/<ScorerName>/OnlyIncludeIfIncidentParticleMomentumNot = 1. MeV
    d:Sc/<ScorerName>/OnlyIncludeIfIncidentParticleMomentumAbove = 10. MeV
    d:Sc/<ScorerName>/OnlyIncludeIfIncidentParticleMomentumNotAbove = 10. MeV
    sv:Sc/<ScorerName>/OnlyIncludeParticlesFromProcess = 2 "hIoni" "eBrem"
    sv:Sc/<ScorerName>/OnlyIncludeParticlesNotFromProcess = 2 "hIoni" "eBrem"
    sv:Sc/<ScorerName>/OnlyIncludeIfParticleOrAncestorFromProcess = 2 "hIoni" "eBrem"
    sv:Sc/<ScorerName>/OnlyIncludeIfParticleOrAncestorNotFromProcess = 2 "hIoni" "eBrem"
    sv:Sc/<ScorerName>/OnlyIncludeParticlesNamed = 2 "proton" "neutron"
    sv:Sc/<ScorerName>/OnlyIncludeParticlesNotNamed = 2 "proton" "neutron"
    sv:Sc/<ScorerName>/OnlyIncludeIfParticleOrAncestorNamed = 1 "neutron"
    sv:Sc/<ScorerName>/OnlyIncludeIfParticleOrAncestorNotNamed = 1 "neutron"
    sv:Sc/<ScorerName>/OnlyIncludeParticlesFromVolume = 1 "Propeller20/Leaf"
    sv:Sc/<ScorerName>/OnlyIncludeParticlesNotFromVolume = 1 "Propeller20/Leaf"
    sv:Sc/<ScorerName>/OnlyIncludeParticlesFromComponent = 1 "Jaws"
    sv:Sc/<ScorerName>/OnlyIncludeParticlesNotFromComponent = 1 "Jaws"
    sv:Sc/<ScorerName>/OnlyIncludeParticlesFromComponentOrSubComponentsOf = 1 "Nozzle"
    sv:Sc/<ScorerName>/OnlyIncludeParticlesNotFromComponentOrSubComponentsOf = 1 "Nozzle"
    sv:Sc/<ScorerName>/OnlyIncludeIfParticleOrAncestorFromVolume = 1 "Propeller20/Leaf"
    sv:Sc/<ScorerName>/OnlyIncludeIfParticleOrAncestorNotFromVolume = 1 "Propeller20/Leaf"
    sv:Sc/<ScorerName>/OnlyIncludeIfParticleOrAncestorFromComponent = 1 "Jaws"
    sv:Sc/<ScorerName>/OnlyIncludeIfParticleOrAncestorNotFromComponent = 1 "Jaws"
    sv:Sc/<ScorerName>/OnlyIncludeIfParticleOrAncestorFromComponentOrSubComponentsOf = 1 "Nozzle"
    sv:Sc/<ScorerName>/OnlyIncludeIfParticleOrAncestorNotFromComponentOrSubComponentsOf = 1 "Nozzle"
    sv:Sc/<ScorerName>/OnlyIncludeIfParticleInteractedInVolume = 1 "Propeller20/Leaf"
    sv:Sc/<ScorerName>/OnlyIncludeIfParticleNotInteractedInVolume = 1 "Propeller20/Leaf"
    sv:Sc/<ScorerName>/OnlyIncludeIfParticleInteractedInComponent = 1 "Jaws"
    sv:Sc/<ScorerName>/OnlyIncludeIfParticleNotInteractedInComponent = 1 "Jaws"
    sv:Sc/<ScorerName>/OnlyIncludeIfParticleInteractedInComponentOrSubComponentsOf = 1 "Nozzle"
    sv:Sc/<ScorerName>/OnlyIncludeIfParticleNotInteractedInComponentOrSubComponentsOf = 1 "Nozzle"
    sv:Sc/<ScorerName>/OnlyIncludeIfParticleOrAncestorInteractedInVolume = 1 "Propeller20/Leaf"
    sv:Sc/<ScorerName>/OnlyIncludeIfParticleOrAncestorNotInteractedInVolume = 1 "Propeller20/Leaf"
    sv:Sc/<ScorerName>/OnlyIncludeIfParticleOrAncestorInteractedInComponent = 1 "Jaws"
    sv:Sc/<ScorerName>/OnlyIncludeIfParticleOrAncestorNotInteractedInComponent = 1 "Jaws"
    sv:Sc/<ScorerName>/OnlyIncludeIfParticleOrAncestorInteractedInComponentOrSubComponentsOf = 1 "Nozzle"
    sv:Sc/<ScorerName>/OnlyIncludeIfParticleOrAncestorNotInteractedInComponentOrSubComponentsOf = 1 "Nozzle"
    sv:Sc/<ScorerName>/OnlyIncludeIfParticleTraversedVolume = 1 "Propeller20/Leaf"
    sv:Sc/<ScorerName>/OnlyIncludeIfParticleNotTraversedVolume = 1 "Propeller20/Leaf"
    sv:Sc/<ScorerName>/OnlyIncludeIfParticleTraversedComponent = 1 "Jaws"
    sv:Sc/<ScorerName>/OnlyIncludeIfParticleNotTraversedComponent = 1 "Jaws"
    sv:Sc/<ScorerName>/OnlyIncludeIfParticleTraversedComponentOrSubComponentsOf = 1 "Nozzle"
    sv:Sc/<ScorerName>/OnlyIncludeIfParticleNotTraversedComponentOrSubComponentsOf = 1 "Nozzle"
    sv:Sc/<ScorerName>/OnlyIncludeIfParticleOrAncestorTraversedVolume = 1 "Propeller20/Leaf"
    sv:Sc/<ScorerName>/OnlyIncludeIfParticleOrAncestorNotTraversedVolume = 1 "Propeller20/Leaf"
    sv:Sc/<ScorerName>/OnlyIncludeIfParticleOrAncestorTraversedComponent = 1 "Jaws"
    sv:Sc/<ScorerName>/OnlyIncludeIfParticleOrAncestorNotTraversedComponent = 1 "Jaws"
    sv:Sc/<ScorerName>/OnlyIncludeIfParticleOrAncestorTraversedComponentOrSubComponentsOf = 1 "Nozzle"
    sv:Sc/<ScorerName>/OnlyIncludeIfParticleOrAncestorNotTraversedComponentOrSubComponentsOf = 1 "Nozzle"
    sv:Sc/<ScorerName>/OnlyIncludeIfInMaterial = 2 "G4_WATER" "Air"
    sv:Sc/<ScorerName>/OnlyIncludeIfNotInMaterial = 2 "G4_WATER" "Air"
    sv:Sc/<ScorerName>/OnlyIncludeIfInRTStructure = 2 "R_LUNG" "L_LUNG"
    s:Sc/<ScorerName>/OnlyIncludeParticlesGoing = "In"
    sv:Sc/<ScorerName>/OnlyIncludeParticlesNamed = 1 "proton"
    d:Sc/<ScorerName>/OnlyIncludeParticlesWithInitialKEAbove = 100. MeV # minimum energy
    sv:Sc/<ScorerName>/OnlyIncludeParticlesNamed = 2 "proton" "neutron"
    d:Sc/<ScorerName>/OnlyIncludeParticlesWithInitialKEAbove = 100. MeV # minimum energy
    b:Sc/<ScorerName>/InvertFilter = "True"
   


Scoring Parameters Used by Output Specification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    s:Sc/<ScorerName>/OutputFile = "myOutputFileName" # if null, use scorer name, e.g. "MyScorer"
    b:Sc/<ScorerName>/OutputAfterRun = "True" # set True to trigger output of scorer after this run
    b:Sc/<ScorerName>/OutputToConsole = "True" # control whether output is also dumped to console
    s:Sc/<ScorerName>/IfOutputFileAlreadyExists = "Increment" # "Exit", "Overwrite" or "Increment"
    b:Sc/<ScorerName>/DICOMOutput32BitsPerPixel = "True"
    s:Sc/<ScorerName>/SeriesDescription = "Custom description here"
    i:Sc/<ScorerName>/HistogramBins = 100 # number of bins
    d:Sc/<ScorerName>/HistogramMin = 0. MeV # with unit appropriate to scored quantity
    d:Sc/<ScorerName>/HistogramMax = 100. MeV # with unit appropriate to scored quantity
    s:Sc/RootFileName = "topas" # name for ROOT output file
    s:Sc/XmlFileName = "topas" # name for XML output file
    sv:Sc/<ScorerName>/Report = 1 "CumulativeVolumeHistogram"
       


Scoring Parameters Used by Miscellaneous Scorers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    i:Sc/<ScorerName>/RBins = 20
    i:Sc/<ScorerName>/PhiBins = 20
    i:Sc/<ScorerName>/ThetaBins = 1
    i:Sc/<ScorerName>/TimeBins = 10 # defaults to 0, that is, un-binned
    d:Sc/<ScorerName>/TimeBinMin = 0. ns # defaults to zero
    d:Sc/<ScorerName>/TimeBinMax = 100. ns # must be specified if TimeBins is greater than 1
    s:Sc/<ScorerName>/SplitByTimeFeature = some_time_feature_name
    dv:Sc/<ScorerName>/SplitByTimeFeatureValues = 5 0. 90. 180. 270. 360. deg
    Sc/DoseAtPhantom-image1
    Sc/DoseAtPhantom-image2
    Sc/DoseAtPhantom-image3
    sv:Sc/<ScorerName>/Report = 1 "Sum" # One or more of Sum, Mean, Histories, Count_In_Bin, Second_Moment, Variance, Standard_Deviation, Min, Max
    s:Sc/<ScorerName>/ColorBy = "Sum" # sum, mean, histories, standard_deviation, min, max
    sv:Sc/<ScorerName>/ColorNames = 5 "white" "grey240" "grey220" "grey200" "grey180"
    dv:Sc/<ScorerName>/ColorValues = 4 1. 1000 2000 3000 MeV
    Sc/<ScorerName>/Active = "False"
    s:Sc/<ScorerName>/InputFile = "MySavedFileName" # match exact case
    s:Sc/<ScorerName>/InputType = "csv"



Graphics Overall Control
~~~~~~~~~~~~~~~~~~~~~~~~

::

    b:Gr/Enable = "True" # Set False to avoid instantiating any part of Geant4 visualization system
    i:Gr/Verbosity = 0 # Set to higher integer to increase verbosity of Geant4 visualization system
    s:Gr/RefreshEvery = "Run" # "History", "Run" or "Session"
    i:Gr/ShowOnlyOutlineIfVoxelCountExceeds = 8000 # Above this limit, only show outer box
    i:Gr/SwitchOGLtoOGLIifVoxelCountExceeds = 70000000 # Above this limit, switch OpenGL Graphics to Immediate mode
    s:Gr/<GraphicsName>/Type = "OpenGL" # OpenGL, HepRep, VRML, DAWN, RayTracer, RayTracerX
    s:Gr/<GraphicsName>/FileName = "MyFileName" # Defaults to name of view (which here is MyGraphic1).
    b:Gr/<GraphicsName>/IncludeGeometry = "True" # defaults to "True"
    b:Gr/<GraphicsName>/IncludeTrajectories = "True" # defaults to "True"
    b:Gr/<GraphicsName>/IncludeStepPoints = "True" # Show trajectory step points, defaults to "False"
    b:Gr/<GraphicsName>/UseSmoothTrajectories = "False" # defaults to "True"
    b:Gr/<GraphicsName>/IncludeAxes = "True" # defaults to "False"
    s:Gr/<GraphicsName>/AxesComponent = "World" # Component in which to center the axes. Defaults to World.
    d:Gr/<GraphicsName>/AxesSize = 3. m # size of axes
    i:Gr/<GraphicsName>/MagneticFieldArrowDensity = 10
    s:Gr/RefreshEvery = "History" # "History", "Run" or "Session"
    sv:Gr/<GraphicsName>/VisibleWorlds = 1 "World" # "World", "All" or one or more specific world names
    b:Gr/<GraphicsName>/Active = "False" # defaults to "True"
    u:Gr/<GraphicsName>/Zoom = 2. # increase to zoom in, decrease to zoom out
    d:Gr/<GraphicsName>/Theta = 45. deg # view angle as in /vis/viewer/set/viewpointThetaPhi
    d:Gr/<GraphicsName>/Phi = 45. deg # view angle as in /vis/viewer/set/viewpointThetaPhi
    u:Gr/<GraphicsName>/TransX = 0. # move left or right in the view window
    d:Gr/<GraphicsName>/TransY = 0. # move up or down in the view window
    s:Gr/<GraphicsName>/Projection = "Perspective" # Defaults to "Orthogonal"
    d:Gr/<GraphicsName>/PerspectiveAngle = 10. deg # Increase for stronger perspective effect
    i:Gr/<GraphicsName>/WindowSizeX = 600
    i:Gr/<GraphicsName>/WindowSizeY = 600
    i:Gr/<GraphicsName>/WindowPosX = 0
    i:Gr/<GraphicsName>/WindowPosY = 0
    b:Gr/<GraphicsName>/HiddenLineRemovalForGeometry = "False" # Remove hidden lines from wireframe geometries, like Geant4’s /vis/viewer/set/hiddenEdge
    b:Gr/<GraphicsName>/HiddenLineRemovalForTrajectories = "False" # Remove hidden trajectories lines from within geometries, like Geant4’s /vis/viewer/set/hiddenMarker
    b:Gr/<GraphicsName>/CopyOpenGLToPDF = "True" # save to PDF
    b:Gr/<GraphicsName>/CopyOpenGLToSVG = "True" # save to Scalable Vector Graphics
    b:Gr/<GraphicsName>/CopyOpenGLToEPS = "True" # save to Encapsulated PostScript
    b:Gr/<GraphicsName>/CopyOpenGLToPS  = "True" # save to PostScript
    s:Gr/<GraphicsName>/ColorBy = "Charge" # "Charge", "ParticleType", "OriginComponent", "Energy", "Momentum", "Generation", "CreatorProcess"
    sv:Gr/<GraphicsName>/ColorByChargeColors = 3 "blue" "green" "red" # colors for neg, neutral, pos
    sv:Gr/<GraphicsName>/ColorByParticleTypeNames = 4 "e-" "gamma" "proton" "neutron" # any number of particle names
    sv:Gr/<GraphicsName>/ColorByParticleTypeColors = 4 "red" "green" "blue" "yellow" # for each particle type above. All other particles will be set to grey.
    sv:Gr/<GraphicsName>/ColorByOriginVolumeNames = 1 "Propeller20/Leaf" # one or more volume
    sv:Gr/<GraphicsName>/ColorByOriginVolumeColors = 1 "red" # one color for each name above
    sv:Gr/<GraphicsName>/ColorByOriginComponentNames = 1 "jaws" # one or more component names
    sv:Gr/<GraphicsName>/ColorByOriginComponentColors = 1 "red" # one color for each name above
    dv:Gr/<GraphicsName>/ColorByEnergyRanges = 3 1. 4. 8. MeV # limits of energy ranges
    sv:Gr/<GraphicsName>/ColorByEnergyColors = 4 "red green blue yellow" # one for every energy interval that is defined by those ranges
    dv:Gr/<GraphicsName>/ColorByMomentumRanges = 3 1. 4. 8. MeV # limits of momentum ranges
    sv:Gr/<GraphicsName>/ColorByMomentumColors = 4 "red" "green" "blue" "yellow" # one for every energy interval that is defined by those ranges
    sv:Gr/<GraphicsName>/ColorByGenerationColors = 2 "red" "green" # colors for primary and secondaries
    sv:Gr/<GraphicsName>/ColorByCreatorProcessNames = 5 "eBrem" "annihil" "Decay" "eIoni" "hIoni" # one or more process name
    sv:Gr/<GraphicsName>/ColorByCreatorProcessColors = 5 "red" "green" "blue" "yellow" "magenta" # one for every process name
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
    sv:Gr/OnlyIncludeParticlesFromVolume
    sv:Gr/OnlyIncludeParticlesFromComponent
    sv:Gr/OnlyIncludeParticlesFromComponentOrSubComponentsOf

    


Graphics for Patient
~~~~~~~~~~~~~~~~~~~~~~~

::

    iv:Gr/<ComponentName>/ShowSpecificSlicesZ = 4 1 3 9 12 # will only show slices 1, 3, 9 and 12
    v:Gr/<ComponentName>/ShowSpecificSlicesZ = 1 0 # means show all slices
    iv:Gr/<ComponentName>/ShowSpecificSlicesZ = 1 -1 # means only show center slice
    iv:Gr/<ComponentName>/ShowSpecificSlicesZ = 1 -2 # means only first, center and last slice
    iv:Gr/<ComponentName>/ShowSpecificSlicesX = 1 -2 # means only show center slice
    iv:Gr/<ComponentName>/ShowSpecificSlicesY = 1 -2 # means only show center slice
    iv:Gr/<ComponentName>/ShowSpecificSlicesZ = 1 -2 # means only show center slice
    i:Gr/ShowOnlyOutlineIfVoxelCountExceeds = 8000
    iv:Gr/<ComponentName>/PatientTissue1 = 3  63 63 63
    iv:Gr/<ComponentName>/PatientTissue2 = 3 100  0  0



Physics List Overall Control
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    s:Ph/ListName = "Default"
    b:Ph/ListProcesses = "False" # Set true to dump list of active physics processes to console
    s:Ph/<PhysicsListName>/Type = "Geant4_Modular"
    sv:Ph/<PhysicsListName>/Modules = 6 "g4em-standard_opt4" "g4h-phy_QGSP_BIC_HP" "g4decay" "g4ion-binarycascade" "g4h-elastic_HP" "g4stopping"
    d:Ph/<PhysicsListName>/EMRangeMin = 100. eV
    d:Ph/<PhysicsListName>/EMRangeMax = 500. MeV
    sv:Ph/<PhysicsListName>/LayeredMassGeometryWorlds = 2 "Tumor" "Seed"
    d:Ph/<PhysicsListName>/CutForElectron = 1 mm # defaults to 0.05 mm



Physics Lists for Type Modular
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    d:Ph/<PhysicsListName>/CutForAllParticles = 0.05 mm # single range cut to use for all particles
    d:Ph/<PhysicsListName>/CutForGamma = 0.05 mm # overrides CutForAllParticles for Gamma
    d:Ph/<PhysicsListName>/CutForElectron = 0.05 mm # overrides CutForAllParticles for Electron
    d:Ph/<PhysicsListName>/CutForPositron = 0.05 mm # overrides CutForAllParticles for Positron
    d:Ph/<PhysicsListName>/CutForProton = 0.05 mm # overrides CutForAllParticles for Proton
    d:Ph/<PhysicsListName>/CutForAlpha = 0.05 mm # overrides CutForAllParticles for Alpha
    d:Ph/<PhysicsListName>/CutForDeuteron = 0.05 mm # overrides CutForAllParticles for Deuteron
    d:Ph/<PhysicsListName>/CutForTriton = 0.05 mm # overrides CutForAllParticles for Triton
    d:Ph/<PhysicsListName>/EMRangeMin = 100. eV # minimum for EM tables
    d:Ph/<PhysicsListName>/EMRangeMax = 500. MeV # maximum for EM tables
    i:Ph/<PhysicsListName>/EMBins = 77 # number of bins for EM tables
    i:Ph/<PhysicsListName>/EMBinsPerDecade = 7 # number of bins per decade for EM tables
    b:Ph/<PhysicsListName>/Fluorescence = "False" # Set to true to turn on Fluorescence
    b:Ph/<PhysicsListName>/Auger = "False" # Set to true to turn on Auger
    b:Ph/<PhysicsListName>/AugerCascade = "False" # Set to true to turn on AugerCascade
    b:Ph/<PhysicsListName>/DeexcitationIgnoreCut = "False" # Set to true to implement DeexcitationIgnoreCut
    b:Ph/<PhysicsListName>/PIXE = "False" # Set to true to turn on PIXE



Physics Lists for Type Optical
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    b:Ma/<PhysicsListName>/EnableOpticalProperties = "True"
    dv:Ma/<PhysicsListName>/RefractiveIndex/Energies = 3 2.0 2.5 3.0 eV
    uv:Ma/<PhysicsListName>/RefractiveIndex/Values = 3 1.58 1.58 1.58
    u:Ma/<PhysicsListName>/ScintillationYield = 1120 # in ph/MeV
    d:Ma/<PhysicsListName>/FastTimeConstant = 2.1 ns



Physics Lists for Type Miscellaneous
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    d:Ph/<PhysicsListName>/SetProductionCutLowerEdge = 200 eV
    d:Ph/<PhysicsListName>/SetProductionCutHighEdge = 30 MeV



Surfaces
~~~~~~~~~

::

    s:Su/<SurfaceName>/Type = "dielectric_dielectric" # or dielectric_metal
    s:Su/<SurfaceName>/Model = "Glisur " # Or Unified
    s:Su/<SurfaceName>/Finish = "Polished"
    dv:Su/<SurfaceName>/Energies = 2 1.0 4.0 eV
    uv:Su/<SurfaceName>/Reflectivity = 2 0.8 0.8



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
    Gr/MyGraphics/Active = "False"
    Ts/PauseBeforeSequence = "True"
        


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
    i:Ma/Verbosity = 1
        


Particle Source
~~~~~~~~~~~~~~~~

::

    i:So/MySource/NumberOfHistoriesInRun = 100
    i:So/MySource/NumberOfHistoriesInRun = 10
    i:So/MySource/NumberOfHistoriesInRun = Tf/MyBCMTimeFeature/Value
    i:So/MySource/NumberOfHistoriesInRandomJob = 1000 # defaults to 100
    d:So/MySource/ProbabilityOfUsingAGivenRandomTime = Tf/MyBCMTimeFeature/Value
    So/MySource/NumberOfHistoriesInRun = 0
            


                



~~~~~~~~~~~~~~~~~~~~~~~~

::

   

    
                



    

   

    
    
    
