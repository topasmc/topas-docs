Custom Imaging to Material Conversion
=====================================

.. highlight:: c++

First line of the cc file must be of the form::

    // Imaging to Material Converter for MyImagingToMaterialConverter1

You can supply your own class to assign imaging values to materials.

To use your Imaging to Material converter, reference its name in the parameter:

.. code-block:: topas

    s:Ge/Patient/ImagingtoMaterialConverter = "MyImagingToMaterialConverter1"

The number of image files read by Topas is determined by the parameter:

.. code-block:: topas

    i:Ge/Patient/NumberOfEnergies = 1 # defaults to 1

If this value is just 1, Topas will look for imaging files directly in your DicomDirectory.
If this value is larger, Topas will expect your DicomDirectory to contain numbered subdirectories:

.. code-block:: plain

    YourDicomDirectory/1
    YourDicomDirectory/2
    etc.

The allowed modalities of the imaging files is determined by the parameter:

.. code-block:: topas

    sv:Ge/Patient/DicomModalityTags = 1 "CT" # defaults to just CT

Other modality tags are, for example, MR for Magnetic Resonance and US for Ultrasound. A complete list can be found `here <https://wiki.cancerimagingarchive.net/display/Public/DICOM+Modality+Abbreviations>`_.

You apply whatever algorithm you like in your class's AssignMaterial method.

This will be called once for each voxel. TOPAS will pass you a vector of imagingValues, with each value representing this voxel's value from one of your image values::

    std::vector< signed short >* imagingValues

For example, if you are doing Dual Energy CT, you will get two values in this vector, the HU values from each of the two CT files.

The materials you use can be defined in your parameter file, in your ImagingToMaterial class's constructor or in your ImagingToMaterial class's AssignMaterial method. Either way, by the time you are finished assigning all of your materials, you will have built up a vector of pointers to materials in fMaterialList and, for each voxel, your AssignMaterials method will have returned an appropriate index into this vector.

AssignMaterials is also passed a timeSliceIndex, which is useful if your imaging is time-dependent (that is, 4D imaging). In this case you can use the timeSliceIndex however you wish in your AssignMaterials algorithm.

To avoid spending CPU time on repeated parameter lookups, it is best to do them in ResolveParameters. Call ResolveParameters directly from your constructor, and then you can also rely on TOPAS to re-call this method any time one of this class's parameters are changed.
