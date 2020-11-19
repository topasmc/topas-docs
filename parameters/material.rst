.. _parameters_material:

Materials
=========

We have :ref:`pre-defined a few materials <parameters_default_materials>`.
You are free to define additional materials, as in::

    sv:Ma/Air/Components=4 "Carbon" "Nitrogen" "Oxygen" "Argon" # names of elements
    uv:Ma/Air/Fractions=4 0.000124 0.755268 0.231781 0.012827 # fractions of elements
    d:Ma/Air/Density=1.2048 mg/cm3
    d:Ma/Air/MeanExcitationEnergy=85.7 eV
    s:Ma/Air/DefaultColor="lightblue"

All :ref:`Elements have been pre-defined <parameters_default_elements>` with natural isotope abundance from the NIST database. You will only need to create your own Elements if you need something other than natural isotope abundance. For that, see :ref:`parameters_element_isotope` below.

``Fractions`` are by weight.

``MeanExcitationEnergy`` is the ``I`` parameter in the Bethe equation, which not only includes ionization, but also inner-atomic excitations, etc.

In the :ref:`parameters_default` section, we show the complete list or pre-defined materials. This basically covers those materials that are used in our included examples.

You may also use any of the Materials and Compounds that are defined by default in Geant4. The names start with the prefix, ``G4_``, such as: ``G4_Al``, ``G4_Ti``, ``G4_MUSCLE_SKELETAL_ICRP``, etc. The complete list of these materials and compounds can be found `here <http://geant4-userdoc.web.cern.ch/geant4-userdoc/UsersGuides/ForApplicationDeveloper/html/Appendix/materialNames.html#g4matrdb>`_.

* NIST material names must be specified with exact case.
* As of this writing, the mean excitation energy listed in the above reference for ``G4_WATER`` is incorrect. It lists ``G4_WATER`` mean excitation energy as 75.0 eV but it is actually set to 78.0 eV.

.. note:: The Geant4-DNA physics processes have special behavior for ``G4_WATER``. They take into account the material's molecular properties rather than just the atomic properties. Accordingly, you should use ``G4_WATER`` rather than defining your own Water, unless you have some other reason to make a specific change (such as changing the mean excitation energy to something other than 78.0 eV).

It is up to you to define any additional materials that you want in your own parameter files.
If you make your own material, make sure to pick a new material name (the string after the ``Ma/``) and make sure that any other parameter file that uses this material includes the file where you defined this material (either directly or through :ref:`parameters_file_chain`). The usual rules of :ref:`parameters_file_graphs` govern parameter conflicts.

.. warning::

    Do not use the prefix ``G4_`` for the materials that you add. This prefix is reserved for materials and compounds from the pre-defined NIST database.

Where a pre-defined material definition exists, it is generally better to use that definition rather than making your own material. The pre-defined material may provide extra benefit by triggering specific corrections to ionization models.

If you have a set of materials that differ only in density, you can define them all at once (this is commonly needed for :ref:`imaging to material conversion <extension_imaging_material_conversion>`)::

    i:Ma/MyMaterial/VariableDensityBins = 100
    u:Ma/MyMaterial/VariableDensityMin = .1
    u:Ma/MyMaterial/VariableDensityMax = 10.

will generate 100 versions of ``MyMaterial``, with densities varying from .1 x normal to 10. x normal. The material names will then be like::

    MyMaterial_VariableDensityBin_0
    MyMaterial_VariableDensityBin_1
    ...
    MyMaterial_VariableDensityBin_99



.. _parameters_element_isotope:

Elements and Isotopes
---------------------

All :ref:`Elements have been pre-defined <parameters_default_elements>` with natural isotope abundance from the NIST database.  You will only need to create your own Elements if you need something other than natural Isotope abundance. You can define additional elements as follows:

Define each isotope that you will use, specifying ``Z``, ``N`` and ``A``::

    i:Is/U235/Z = 92
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
