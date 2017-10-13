.. _parameters_outcome:

Outcome Modeling
================

TOPAS can now directly perform Outcome Modeling such as calculating Tumor Control Probabilities and Normal Tissue Complication Probabilities.

Expanding on TOPAS previous capability to directly produce a Dose Volume Histogram,
TOPAS can now directly apply outcome models to the DVH.
We provide a variety of standard outcome models from the literature,
for each of which you can adjust various parameters.
You can also write your own outcome models using the TOPAS Extensions interface.

Starting from an existing scorer, if a differential or cumulative histogram will be scored, TOPAS will takes the corresponding bins (dose and volume) as input of the biological models::

    s:Sc/ScorerName/Report= "differentialvolumehistogram" # or "cumulativevolumehistogram"

An example that runs several different outcome models on a patient dose can be seen at :ref:`example_outcome_testoutcomemodel`

We also allow you to read back in a previously created DVH to have TOPAS apply new outcome models without having to re-do the Monte Carlo simulation phase of the job. Just set the parameter that tells TOPAS to restore results from a previously created file::

    Ts/RestoreResultsFromFile = "True"

See the example :ref:`example_outcome_testrestoremodel`

If no volume histogram is required, as input of the biological models, TOPAS will takes the final full dose distribution in the organ, and by assuming that all voxels have the same dimension, the volume input will be a vector of ones. This assumption relies in the fact that volume bins are internally converted to fractional volume.

To activate the biological models calculation::

    b:Sc/ScorerName/CalculateProbabilityOfOutcome = "True"

User may want to scale the dose distribution::

    u:Sc/ScorerName/BiologyOutputScaleFactor = 1E6

Set the number and name of models to be calculated::

    sv:Sc/ScorerName/ModelName = 2 "LKB" "CriticalElement"

Set the input parameters of the corresponding model::

    u:Sc/ScorerName/LKB/n = 0.25
    u:Sc/ScorerName/LKB/m = 0.15
    u:Sc/ScorerName/LKB/td50 = 60
    u:Sc/ScorerName/CriticalElement/m = 0.15
    u:Sc/ScorerName/CriticalElement/td50 = 60
    s:Sc/ScorerName/CriticalElement/Function="probit" #"logistic"

For LKB, critical element, critical volume and Poisson models, the parameters can be set from an internal data base (see references below) by input the organ name instead of the model parameters as follows::

    s:Sc/ScorerName/IncludeParametersFromOrganNamed="brain"

If the organ name is not found, the full list of available names is displayed and TOPAS execution is stopped.

The output (NTCP or TCP in percent) will be displayed on the screen for every model for every scorer. If CSV or Binary DVHs output is chosen, the output will be at the header too.

The follow references contains tables with parameters for several organs for several models::

    C. Burman, G. J. Kutcher, B. Emami and M. Goitein, “Fitting of normal tissue tolerance data to an analytic function”, Int. J. Radiation Oncology Biol. Phys. 21, 123-135. (1991)
    B. Emami, J. Lyman, A. Brown, L. Coia, M. Goitein, J. E. Munzenrider, B. Shank. L. J. Solin and M Wesson “Tolerance of normal tissue to therapeutic irradiation”, Int. J. Radiation Oncology Biol. Phys. 21, 109-122. (1991)
    P. Okunieff, D. Morgan, A. Niemerko and D. Suit “Radiation dose-response of human tumors”, Int. J. Radiation Oncology Biol. Phys. 32(4), 1227-1237. (1995)
    P. Stavrev, A. Niemerko, N. Stavreva and M. Goitein, “The application of biological models to clinical data”, Physica Medica, 17(2), 2-13. (2001)
