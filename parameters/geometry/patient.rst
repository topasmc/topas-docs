Patient Components
------------------

TOPAS currently supports the following Patient Component types:

=========================== ========================
Geometry Component          Type
=========================== ========================
:ref:`geometry_dicom`       TsDicomPatient
:ref:`geometry_xio`         TsXioPatient
=========================== ========================

It is also necessary to define how to convert the imaging data to material data, following a :ref:`imaging_material_conversion` scheme.



.. _geometry_patient_common:

Common Parameters
~~~~~~~~~~~~~~~~~

Many of the parameters for Patient Components are common to both TsDicomPatient and TsXioPatient. These are described here.

To perform Monte Carlo simulation, TOPAS needs to map each voxel of the patient image to a material, density and, for useful graphics, a color.
You specify how to do this by telling TOPAS which :ref:`imaging_material_conversion` to use.

To dump your file's raw imaging values to the console::

    b:Ge/Patient/DumpImagingValues = "True"

Set any parent you like, but it is often convenient to place patient into a group component which can then be rotated to represent couch setup::

    s:Ge/Patient/Parent = "PatientGroup"

.. todo:: Remove need for ``Ge/Patient/Material`` parameter

.. warning::

    We will eventually get rid of the ``Ge/Patient/Material`` parameter, but for now, you need to provide one, though it doesn’t really matter what value it has. The actual voxel materials will come from the :ref:`imaging_material_conversion`.

Even though a large number of materials are defined in your HU conversion file, TOPAS will only create those materials that are actually used in your CT image.
In the 4DCT case, if any image introduces new materials that were not in the first image, Geant4 will be unable to proceed (it cannot load new materials after physics has initialized). TOPAS will exit with a warning message advising you to set the parameter::

    b:Ge/Patient/PreLoadAllMaterials = "True"

Startup will then be slower, since TOPAS will preload the full set of materials defined in your HU conversion file, but your 4DCT will then work.

For single slice thickness images, scoring will use the same voxel divisions as your CT image.
For multiple slice thicknesses, scoring will not know what divisions to use unless you explicitly specify these in your scoring parameters, such as::

    i:Sc/MyScorer/XBins = 512
    i:Sc/MyScorer/YBins = 512
    i:Sc/MyScorer/ZBins = 256

The built-in Geant4 visualization tools do not perform well when a complex voxel structure is loaded. To make visualization more successful, several additional parameters are provided.

There is generally little value in showing all pixels of the image at once. Each slice just covers up the last slice. To instead show only a specific set of slices in any dimension::

    iv:Gr/Patient/ShowSpecificSlicesZ = 4 1 3 9 12 # will only show slices 1, 3, 9 and 12.

Similar slicing is allowed in X and Y.
Three special values are also allowed::

    iv:Gr/Patient/ShowSpecificSlicesZ = 1 0 # means show all slices
    iv:Gr/Patient/ShowSpecificSlicesZ = 1 -1 # means only show center slice
    iv:Gr/Patient/ShowSpecificSlicesZ = 1 -2 # means only first, center and last slice

The following will result in a display that shows 27 pixels comprising the boundaries and center of the image. This allows you to see the overall placement of the image and see the individual voxel size::

    iv:Gr/Patient/ShowSpecificSlicesX = 1 -2 # means only show center slice
    iv:Gr/Patient/ShowSpecificSlicesY = 1 -2 # means only show center slice
    iv:Gr/Patient/ShowSpecificSlicesZ = 1 -2 # means only show center slice

Another option allows you to specify the maximum number of voxels to show. If the total number of voxels is greater than this limit, TOPAS will just draw the overall DICOM outline::

    i:Gr/ShowOnlyOutlineIfVoxelCountExceeds = 10000

By default, OpenGL graphics switches its fast "Stored" mode to its more memory efficient "Immediate" mode when the graphics scene gets very complicated. When this switch occurs, the current version of Geant4 has a bug such that part of the image is lost. To prevent this from impacting DICOM images, you can set a threshold at which Geant4 will use Immediate mode from the start::

    i:Gr/SwitchOGLtoOGLIifVoxelCountExceeds = 10000 # Above this limit, switch OpenGL Graphics to Immediate mode



.. _geometry_dicom:

Patient in DICOM Format
~~~~~~~~~~~~~~~~~~~~~~~

DICOM import is handled through the `GDCM <http://gdcm.sourceforge.net>`_ package, which is pre-built into TOPAS.

See the :ref:`example_dicom` and :ref:`example_dicom_time` examples of how to use TsDicomPatient. Note that before running this example, you must unzip the included DICOM files.

You specify the name of a directory containing one or more dcm files (one for each slice)::

    s:Ge/Patient/DicomDirectory = "DICOM_Box"

To specify 4DCT, you can have DicomDirectory change under control of a :ref:`Time Feature <time_feature>`.

Files of other types in this directory will be ignored.
Exact titles of the dcm files are not important as TOPAS will re-order them based on the slice ordering information inside the DICOM headers.

By default, Topas will only consider dcm files that are from CT. This can be adjusted by::

    sv:Ge/Patient/DicomModalityTags = 1 "CT" # defaults to just CT

Other modality tags are, for example, ``"MR"`` for Magnetic Resonance and ``"US"`` for Ultrasound. A complete list can be found `here <https://wiki.cancerimagingarchive.net/display/Public/DICOM+Modality+Abbreviations>`_.

Patient positioning information from the DICOM file is not currently used. You must position as you would for any TOPAS component::

    d:Ge/Patient/TransX=0. m
    d:Ge/Patient/TransY=0. m
    d:Ge/Patient/TransZ=0. m
    d:Ge/Patient/RotX=0. deg
    d:Ge/Patient/RotY=0. deg
    d:Ge/Patient/RotZ=0. deg

TOPAS can read DICOM RT Structure Sets.
A structure set is an extra file in the DICOM directory that provides information on structures such as organs, tumors, PTVs, etc. that have been outlined (contoured) in the planning process. The data is stored as a set of polygons, up to one per slice for each contoured structure. TOPAS can color code DICOM components according to this structure information and can filter scoring based on these structures (see the filter: OnlyIncludeIfInRTStructure).

.. todo:: DICOM RTSTRUCT actually supports multiple polygons per structure per slice

To make TOPAS color the voxels by structure::

    sv:Ge/Patient/ColorByRTStructNames = 2 "R_LUNG" "L_LUNG"
    sv:Ge/Patient/ColorByRTStructColors = 2 "yellow" "red"

* If the structure name includes a space, substitute an underscore in the parameter. So, for example, if the structure name is "R LUNG", you should supply the parameter as "R_LUNG".
* If you don’t actually know what structures are included in your DICOM, just try providing in ``ColorByRTStructNames``. TOPAS will give you an error message that includes a list of the known structure names.
* To allow easy testing of this feature in simple DICOM examples that don’t really have any structures, the following parameter will "fake" an RT structure set, assigning the given structure to all voxels in the lower XY quadrant::

    b:Ge/Patient/FakeStructures = "True"



.. _geometry_xio:

Patient in XiO Format
~~~~~~~~~~~~~~~~~~~~~

The XiO patient is a specific implementation of a patient geometry. It requires a binary file containing a list of Hounsfield units for each voxel of a patient in "short little endian" format.

See the :ref:`example_dicom` example of how to use TsXiOPatient.

Specify file directory and file name::

    s:Ge/Patient/InputDirectory = "./"
    s:Ge/Patient/InputFile = "ctvolume.dat" # match exact case

To specify 4DCT, you can have ``InputDirectory`` or ``InputFile`` change under control of a :ref:`Time Feature <time_feature>`.

You must position as you would for any TOPAS component::

    d:Ge/Patient/RotX = 0. deg
    d:Ge/Patient/RotY = 90. deg
    d:Ge/Patient/RotZ = 0. deg
    d:Ge/Patient/TransX = 1.5 mm
    d:Ge/Patient/TransY = 3.3 mm
    d:Ge/Patient/TransZ = 4.2 mm

XiO Format does not contain voxel number and size information. You must specify it as follows.

Number and size of voxels in X and Y::

    i:Ge/Patient/NumberOfVoxelsX = 25
    i:Ge/Patient/NumberOfVoxelsY = 25
    d:Ge/Patient/VoxelSizeX = 2.0 mm
    d:Ge/Patient/VoxelSizeY = 2.0 mm

Number and size of Voxels in Z are vectors rather than single values since XiO file may have multiple slice thickness sections.

If there is only one slice thickness in your image, just specify one element::

    iv:Ge/Patient/NumberOfVoxelsZ = 1 10
    dv:Ge/Patient/VoxelSizeZ = 1 2.5 mm

If there are multiple slice thicknesses in your image, specify number and thickness of voxels in each section. For example, a 30 slice image that has 10 slices of 2.5 mm and then 20 slices of 1.25 mm::

    iv:Ge/Patient/NumberOfVoxelsZ = 2 10 20
    dv:Ge/Patient/VoxelSizeZ = 2 2.5 1.25 mm



.. _imaging_material_conversion:

Imaging to Material Conversion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You are free to write your own converter, including approaches that use alternative imaging modalities (e.g. MRI, pCT, ultrasound), or that use more than one image (e.g. Dual Energy CT, Multi-Energy CT). To write your own converter, see :ref:`extension_imaging_material_conversion`.

TOPAS provides one built-in converter, that follows the most common method used in proton therapy (`PubMed <http://www.ncbi.nlm.nih.gov/pubmed/10701515>`_):

* Schneider W, Bortfeld T and Schlegel W. Correlation between CT numbers and tissue parameters needed for Monte Carlo simulations of clinical dose distributions. Phys. Med. Biol. 2000; 45(2):459-78.

This converter follows the technique developed by Schneider to assign materials based on a single CT image file containing Hounsfield Unit (HU) values. It is selected using::

    s:Ge/Patient/ImagingtoMaterialConverter = "Schneider"

The HU conversion parameters are typically stored in a separate parameter file::

    includeFile = HUtoMaterialSchneider.txt

An example of such a HU conversion parameter file is examples/DICOM/HUtoMaterialSchneider.txt.

The first set of parameters in the HU file are used to calculate density::

    dv:Ge/Patient/DensityCorrection = 3996 9.35212 5.55269 4.14652 ...1.06255 1.00275 g/cm3
    iv:Ge/Patient/SchneiderHounsfieldUnitSections = 8 -1000 -98 15 23 101 2001 2995 2996
    uv:Ge/Patient/SchneiderDensityOffset = 7 0.00121 1.018 1.03 1.003 1.017 2.201 4.54
    uv:Ge/Patient/SchneiderDensityFactor = 7 0.00103 0.00089 0.0 0.00117 0.00059 0.0005 0.0
    uv:Ge/Patient/SchneiderDensityFactorOffset = 7 1000. 0. 1000. 0. 0. -2000. 0.

``DensityCorrection``:

* One value for every possible HU value.
* Values start from ``Ge/Patient/MinImagingValue`` which defaults to -1000

``SchneiderHounsfieldUnitSections``:

* Specifies how to break up the entire set of HU units into several density calculation sections. The HU conversion formula then uses different correction factors for each of these sections.
* The total range (last value minus first value) must equal the number of values in ``DensityCorrection``.
* In the above example, the 8 values define 7 sections:

    * Section 1: -1000 to -99
    * Section 2: -98 to 14
    * ...
    * Section 7: 2995 to 2996

``SchneiderDensityOffset``, ``SchneiderDensityFactor`` and ``SchneiderDensityFactorOffset``:

* Must have one value for each of the density calculation sections, so length must be one less than the length of ``SchneiderHounsfieldUnitSections``

Thus, for any specific HU number, we can extract the appropriate:

* DensityCorrection
* SchneiderDensityOffset
* SchneiderDensityFactor
* SchneiderDensityFactorOffset

And use these in the Schneider formula:

* Density = ( Offset + ( Factor * ( FactorOffset + HU[-1000,2995] ) ) ) * DensityCorrection

The second set of parameters in the HU file are used to calculate material name and graphics color::

    iv:Ge/Patient/SchneiderHUToMaterialSections = 26 -1000 -950 -120 -83 ... 1500 2995 2996
    sv:Ge/Patient/SchneiderElements = 13 "Hydrogen" "Carbon" "Nitrogen" "Oxygen" ...
    uv:Ge/Patient/SchneiderMaterialsWeight1 = 13 0.0   0.0   0.755 0.232 ...
    uv:Ge/Patient/SchneiderMaterialsWeight2 = 13 0.103 0.105 0.031 0.749 ...
    ...
    iv:Gr/Color/PatientTissue1 = 3  63 63 63
    iv:Gr/Color/PatientTissue2 = 3 100  0  0
    ...

``iv:SchneiderHUToMaterialSections``:

* Specifies how to break up the entire set of HU units into several material name assignment sections.
* The total range (last value minus first value) must equal the number of values in ``DensityCorrection``.
* In the above example, the 26 values define 7 material name assignment sections:

    * Section 1: -1000 to -949
    * Section 2: -50 to -119
    * ...
    * Section 26: 2995 to 2996

``sv:SchneiderElements``:

* Specifies all of the elements that will be used in the patient.
* All patient materials must be composed from combinations of this set of elements.

``uv:SchneiderMaterialsWeight1`` through ``SchneiderMaterialsWeight26``:

* There should be one of these parameters for each of the material name assignment sections. The length of ``SchneiderMaterialsWeight`` must equal the length of ``SchneiderElements``.
* Each value in ``SchneiderMaterialsWeight`` tells what proportion of the given element in ``SchneiderElements`` to use in this material.
* In our ``SchneiderMaterialsWeight2`` parameter, the values: 0.103 0.105 0.031 0.749 mean:

    * 10.3 percent of the first element, Hydrogen
    * 10.5 percent of the second element, Carbon
    * 3.1 percent of the second element, Nitrogen
    * 74.9 percent of the second element, Oxygen

``dv:SchneiderMaterialMeanExcitationEnergy``:

* You may optionally provide this parameter to override the default mean excitation energies of some or all of the materials.
* There should be one value for each material name assignment section.
* To use the default mean excitation energy for a particular material, enter that value as 0.
* For example, the following just overrides defaults for two out of 26 assignment sections::

    dv:Ge/Patient/SchneiderMaterialMeanExcitationEnergy = 26 88.8 0. 77.7. 0. 0. 0. 0. 0.
    0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. eV

``iv:Gr/Color/PatientTissue1``:

* Specifies what colors should be assigned to each of the materials.
* There should be one of these parameters for each of the ``SchneiderHUToMaterialSections``.
* The three values specify the Red, Green and Blue components of the color.

Putting it all together, we have now specified density, material name, color and, optionally, mean excitation energy, for each of the Hounsfield numbers in the patient.

You can review the materials definitions that TOPAS created based on your patient file and the HU conversion settings. The following parameter tells TOPAS to dump parameters to a file::

    Ts/DumpNonDefaultParameters = "True"

For each HU number that was used in the patient file, you will see a set of parameters starting with ``Ma/PatientTissueFromHU-`` followed by an HU number.
For example, for HU number 295, you may see::

    Ma/PatientTissueFromHU-295/Component = 9 Hydrogen Carbon Nitrogen Oxygen Phosphorus Sulfur Chlorine Sodium Potassium
    Ma/PatientTissueFromHU-295/Fractions = 9 0.103 0.105 0.031 0.749 0.002 0.003 0.003 0.002 0.002
    Ma/PatientTissueFromHU-295/Density = 0.707487 g/cm3
    Ma/PatientTissueFromHU-295/DefaultColor = PatientTissue2

where you then follow the ``DefaultColor`` parameter named ``PatientTissue2`` to see that ``Gr/Color/PatientTissue2`` is ``3 100 0 0`` which means a mixture of 100 percent Red, 0 percent green, 0 percent blue.
