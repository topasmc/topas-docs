.. _parameters_material:

Materials
=========

We have pre-defined a few materials.
You are free to define additional materials, as in::

    sv:Ma/Air/Components=4 "Carbon" "Nitrogen" "Oxygen" "Argon" # names of elements
    uv:Ma/Air/Fractions=4 0.000124 0.755268 0.231781 0.012827 # fractions of elements
    d:Ma/Air/Density=1.2048 mg/cm3
    d:Ma/Air/MeanExcitationEnergy=85.7 eV
    s:Ma/Air/DefaultColor="lightblue"

All Elements have been pre-defined with natural isotope abundance from the NIST database.  You will only need to create your own Elements if you need something other than natural Isotope abundance. For that, see Elements and Isotopes below.

Fractions are by weight.

MeanExcitationEnergy is the I parameter in the Bethe equation, which not only includes ionization, but also inner-atomic excitations, etc.

In the :ref:`parameters_default` section, we show the complete list or pre-defined materials. This basically covers those materials that are used in our included examples.

You may also use any of the Materials and Compounds that are defined by default in Geant4. The names start with the prefix, ``G4_``, such as: ``G4_Al``, ``G4_Ti``, ``G4_MUSCLE_SKELETAL_ICRP``, etc. The complete list of these materials and compounds can be found `here <http://geant4.web.cern.ch/geant4/workAreaUserDocKA/Backup/Docbook_UsersGuides_beta/ForApplicationDeveloper/html/apas08.html>`_.

* NIST material names must be specified with exact case.
* As of this writing, the mean excitation energy listed in the above reference for ``G4_WATER`` is incorrect. It lists ``G4_WATER`` mean excitation energy as 75.0 eV but it is actually set to 78.0 eV.

.. note:: The Geant4-DNA physics processes have special behavior for ``G4_WATER``. They take into account the material's molecular properties rather than just the atomic properties. Accordingly, you should use ``G4_WATER`` rather than defining your own Water, unless you have some other reason to make a specific change (such as changing the mean excitation energy to something other than 78.0 eV).

It is up to you to define any additional materials that you want in your own parameter files.
If you make your own material, make sure to pick a new material name (the string after the ``Ma/``) and make sure that any other parameter file that uses this material includes the file where you defined this material (either directly or through a chain of includes).

Do not use the prefix ``G4_`` for the materials that you add. This prefix is reserved for materials and compounds from the pre-defined NIST database.

Where a pre-defined material definition exists, it is generally better to use that definition rather than making your own material. The pre-defined material may provide extra benefit by triggering specific corrections to ionization models.

If you redefine any of the default materials, the normal rules of parameter chains apply: the file with the new definition has to be at the base of all of the chains (otherwise you have an ambiguous situation). So, for example, if file A includes files B and C:

* You can not re-define a default material in file B or C
* You can re-define a default material in file D, that is included by both B and C

If you have a set of materials that differ only in density, you can define them all at once (this is a common need for imaging to material conversion)::

    i:Ma/MyMaterial/VariableDensityBins = 100
    u:Ma/MyMaterial/VariableDensityMin = .1
    u:Ma/MyMaterial/VariableDensityMax = 10.

will generate 100 versions of MyMaterial, with densities varying from .1 x normal to 10. x normal. The material names will then be like::

    MyMaterial_VariableDensityBin_0
    MyMaterial_VariableDensityBin_1
    ...
    MyMaterial_VariableDensityBin_99




Elements and Isotopes
---------------------

All Elements have been pre-defined with natural isotope abundance from the NIST database.  You will only need to create your own Elements if you need something other than natural Isotope abundance. You can define additional elements as follows:

Define each Isotope that you will use, specifying Z, N and A::

    :Is/U235/Z = 92
    i:Is/U235/N = 235
    d:Is/U235/A = 235.01 g/mole
    i:Is/U238/Z = 92
    i:Is/U238/N = 238
    d:Is/U238/A = 238.03 g/mole

Define your element with your desired proportion of these isotopes::

    s:El/MyEIU/Symbol = "MyElU"
    sv:El/MyElU/IsotopeNames = 2 "U235" "U238"
    uv:El/MyElU/IsotopeAbundances = 2 90. 10.

See :ref:`example_basic_isotope` example.
