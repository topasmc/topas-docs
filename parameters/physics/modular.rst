.. _physics_modular:

Modular Physics Lists
---------------------

The default list we provide is a Modular physics list. It is specified by the parameters described :ref:`here <parameters_default_physics>`.

The Geant4 EM physics group recommends against setting ``EMRangeMin`` too low:

* Set to 100. eV or greater when using standard Geant4 EM physics
* Set to 10. eV or greater when using Geant4-DNA physics

If you want to run with no physics, but only the transportation process (useful for some demos and tests), specify the modules in the following special way::

    sv:Ph/Default/Modules = 1 "Transportation_Only"

Below is a :ref:`physics_available_modules` with the corresponding Geant4 class names.

The remaining options for the ``"Geant4_Modular"`` physics type are::

    d:Ph/Default/CutForAllParticles = 0.05 mm # single range cut to use for all particles
    d:Ph/Default/CutForGamma = 0.05 mm # overrides CutForAllParticles for Gamma
    d:Ph/Default/CutForElectron = 0.05 mm # overrides CutForAllParticles for Electron
    d:Ph/Default/CutForPositron = 0.05 mm # overrides CutForAllParticles for Positron
    d:Ph/Default/CutForProton = 0.05 mm # overrides CutForAllParticles for Proton
    d:Ph/Default/CutForAlpha = 0.05 mm # overrides CutForAllParticles for Alpha
    d:Ph/Default/CutForDeuteron = 0.05 mm # overrides CutForAllParticles for Deuteron
    d:Ph/Default/CutForTriton = 0.05 mm # overrides CutForAllParticles for Triton
    d:Ph/Default/EMRangeMin = 100. eV # minimum for EM tables
    d:Ph/Default/EMRangeMax = 300. MeV # maximum for EM tables
    i:Ph/Default/dEdXBins = 220 # number of bins for dEdX tables
    i:Ph/Default/LambdaBins = 220 # number of Lambda bins
    b:Ph/Default/Fluorescence = "False" # Set to true to turn on Fluorescence
    b:Ph/Default/Auger = "False" # Set to true to turn on Auger
    b:Ph/Default/PIXE = "False" # Set to true to turn on PIXE



.. _physics_regions:

Physics Regions
~~~~~~~~~~~~~~~

By default, cuts affect the entire world, but you can optionally divide the world into several regions and can specify different cuts in each region. First, specify which components belong to a given region::

    s:Ge/MyComponent/AssignToRegionNamed = "MyRegion"

* All children of this component will also be assigned to that region, unless the child has its own ``AssignToRegionNamed`` parameter.
* There is no requirement that all of the components in a given region be contiguous.

Then assign cuts per region by including the region name in the parameter name as in::

    d:Ph/Default/ForRegion/MyRegion/CutForGamma = 0.05 mm
    d:Ph/Default/ForRegion/MyRegion/CutForElectron = 0.05 mm
    d:Ph/Default/ForRegion/MyRegion/CutForPositron = 0.05 mm
    d:Ph/Default/ForRegion/MyRegion/CutForProton = 0.05 mm

Cuts do not affect all processes, but only those listed below:

* Energy thresholds for gamma are used in Bremsstrahlung
* Energy thresholds for electrons are used in ionization and e+e- pair production processes Energy thresholds for positrons are used in e+e- pair production process
* Energy thresholds for gamma and electrons are used optionally in all discrete processes

    * Photoelectriceffect
    * Compton
    * gamma conversion

* Energy thresholds for protons are used in processes of elastic scattering for hadrons and ions defining the threshold for kinetic energy of nuclear recoil



.. _physics_available_modules:

List of Available Modules
~~~~~~~~~~~~~~~~~~~~~~~~~

==========================  ===========================
TOPAS Module Name           Geant4 Class Name
==========================  ===========================
g4h-chargeexchange          G4ChargeExchangePhysics
g4decay                     G4DecayPhysics
g4em-dna                    G4EmDNAPhysics
g4em-extra                  G4EmExtraPhysics
g4em-livermore              G4EmLivermorePhysics
g4em-polarized              G4EmLivermorePolarizedPhysics
g4em-lowep                  G4EmLowEPPhysics
g4em-penelope               G4EmPenelopePhysics
g4em-standard_opt0          G4EmStandardPhysics
g4em-standard_opt1          G4EMStandardPhysics_option1
g4em-standard_opt2          G4EMStandardPhysics_option2
g4em-standard_opt3          G4EMStandardPhysics_option3
g4em-standard_opt4          G4EMStandardPhysics_option4
g4em-standard_WVI           G4EmStandardPhysicsWVI
g4h-elastic_D               G4HadronDElasticPhysics
g4h-elastic                 G4HadronElasticPhysics
g4h-elastic_HP              G4HadronElasticPhysicsHP
g4h-elastic_LEND            G4HadronElasticPhysicsLEND
g4h-elastic_XS              G4HadronElasticPhysicsXS
g4h-elastic_H               G4HadronHElasticPhysics
g4h-inelastic_QBBC          G4HadronInelasticQBBC
g4h-phy_FTFP_BERT           HadronPhysicsFTFP_BERT
g4h-phy_FTFP_BERT_HP        HadronPhysicsFTFP_BERT_HP
g4h-phy_FTFP_BERT_TRV       HadronPhysicsFTFP_BERT_TRV
g4h-phy_FTF_BIC             HadronPhysicsFTF_BIC
g4h-phy_QGSP_BERT           HadronPhysicsQGSP_BERT
g4h-phy_QGSP_BERT_HP        HadronPhysicsQGSP_BERT_HP
g4h-phy_QGSP_BIC            HadronPhysicsQGSP_BIC
g4h-phy_QGSP_BIC_HP         HadronPhysicsQGSP_BIC_HP
g4h-phy_QGSP_FTFP_BERT      HadronPhysicsQGSP_FTFP_BERT
g4h-phy_QGS_BIC             HadronPhysicsQGS_BIC
g4h-phy_Shielding           HadronPhysicsShielding
g4ion-binarycascade         G4IonBinaryCascadePhysics
g4ion-inclxx                G4IonINCLXXPhysics
g4ion                       G4IonPhysics
g4ion-QMD                   G4IonQMDPhysics
g4n-trackingcut             G4NeutronTrackingCut
g4optical                   G4OpticalPhysics
g4radioactivedecay          G4RadioactiveDecayPhysics
g4stopping                  G4StoppingPhysics
==========================  ===========================
