Output Specification
--------------------

Scored quantities can be output to simple files (csv or binary formats), data files for use in analysis systems (ROOT or XML format) or to a DICOM file.
There are also options to directly produce Volume Histograms (such as DVH).

To specify output file name::

    s:Sc/MyScorer/OutputFile = "myOutputFileName" # if null, use scorer name, e.g. "MyScorer"

Note that this can be more than just a file name - it can include a relative or absolute file path, as in::

    s:Sc/MyScorer/OutputFile = "../myOutputFileName" # one directory above current directory
    s:Sc/MyScorer/OutputFile = "~/SomeSubdirectory/myOutputFileName"

To specify output file type for all except the :ref:`scoring_phasespace`::

    s:Sc/MyScorer/OutputType = "csv" # "csv", "binary", "Root", "Xml" or "DICOM"

For binary output of 3D data, such as from scoring in a water phantom or a patient, the following table shows the correspondence between TOPAS divisions and common 3D data viewing applications:

+-----------+--------------+-------------------+-------------------+
| TOPAS     |  fNi (X/R/R) |  fNj (Y/Phi/Phi)  |  fNk (Z/Z/Theta)  |
+===========+==============+===================+===================+
| ImageJ    |  Width       |  Height           |  Images           |
+-----------+--------------+-------------------+-------------------+
| ParaView  |  X           |  Y                |  Z                |
+-----------+--------------+-------------------+-------------------+
| Amide     |  X           |  Y                |  Z                |
+-----------+--------------+-------------------+-------------------+
| Numpy     |  Use the python module topas2numpy_                  |
+-----------+--------------+-------------------+-------------------+

.. _topas2numpy: http://topas2numpy.readthedocs.io


DICOM export is handled through the package GDCM_, which is pre-built into TOPAS.

.. _GDCM: http://gdcm.sourceforge.net

DICOM output is in the form of a single .dcm file that contains DICOM header information (voxel size, spacing, etc.) and then a block of binary image data representing the 3D output.
We use the DICOM output format called ``MONOCHROME2``.
Each pixel is represented by a 16 or 32 bit integer.

* 16 bit is the default.
* For 32 bit, specify::

    b:Sc/MyScorer/DICOMOutput32BitsPerPixel = "True"

Because TOPAS accumulates all scores as doubles, you must tell TOPAS how to convert these double values to the DICOM 16bit or 32bit integers. You do so by providing a scaling factor::

    u:Sc/MyScorer/DICOMOutputScaleFactor = 1.0E12

The appropriate value depends on your specific setup. You need a factor that will make your expected double values fit into an appropriate range of 16bit or 32bit integers:

* 16bit integers are 0 through 65,536
* 32bit integers are 0 through 4,294,967,296
* For example, if you expect to score values that are only on the order of 1.0E-9, and you are using 16bit, an output scale factor of 1.0E12 will give you reasonable integers on order of 1000

"Root" and "Xml" will generate histogram files. Specify the binning of the scored quantity as follows::

    i:Sc/MyScorer/HistogramBins = 100 # number of bins
    d:Sc/MyScorer/HistogramMin = 0. MeV # with unit appropriate to scored quantity
    d:Sc/MyScorer/HistogramMax = 100. MeV # with unit appropriate to scored quantity

Histograms will be either 1D or 2D depending on how the scoring geometry is divided or the energy is binned (see :ref:`scoring_binning_energy`).

* If the geometry is undivided and there is no energy binning, a 1D histogram is produced.
* If the geometry is undivided and there is energy binning, the second histogram axes will be energy.
* If the geometry is divided, it can only be divided in one dimension (such as either X, Y or Z for TsBox geometries) and there can be no energy binning. The second histogram axes will be the axes of the geometry division.

All histogram output is combined into a single file, such as ``topas.root`` or ``topas.xml``. The histogram file name can be adjusted by::

    s:Sc/RootFileName = "topas" # name for ROOT output file
    s:Sc/XmlFileName = "topas" # name for XML output file

Physicists often report the quality of a treatment plan by showing Dose Volume Histograms (DVHs). Such histograms represent what fractional volume of a given structure has received a given Dose.

* In a differential DVH, the bin value indicates what percentage of the structure volume received the given dose.
* In a cumulative DVH, the bin value indicates what percentage of the structure volume received at least the given dose (the zeroth bin will always have a value of 1, since all bins receive at least zero dose).
* If you combine TOPAS DVH options with the filtering option ``OnlyIncludeIfInRTStructure`` (see :ref:`scoring_filter`), you can generate a DVH for a specific contoured structure (such as DVH to R_LUNG).

TOPAS can generate a Volume Histogram for any scored quantity, not just Dose. Just set the scorer's report parameter to include either ``"DifferentialVolumeHistogram"`` or ``"CumulativeVolumeHistogram"``, as in::

    sv:Sc/DoseAtPhantom/Report = 1 "CumulativeVolumeHistogram"

You cannot specify both types of volume histograms in a single scorer, but you can specify other reporting options, such as the following, which will give a basic histogram of ``"Sum"`` and ``"Mean"``, plus a ``"CumulativeVolumeHistogram"``::

    sv:Sc/DoseAtPhantom/Report = 3 "Sum" "Mean" "CumulativeVolumeHistogram"

As with any histogram, you also need to specify ``HistogramBins``, ``HistogramMin`` and ``HistogramMax``. For an example, see :ref:`example_scoring_DVH`.

If your results has a 1 in the first bin and zero in the other bins, it probably means your ``HistogramMax`` was set too high, and thus none of the voxels had enough dose to get beyond the zeroth bin.

To specify output file type for the phase space scorer::

    s:Sc/MyScorer/OutputType = "ASCII" # "ASCII" or "Binary"

ASCII format has the advantage that it is human-readable text.
Binary format has the advantage that it is much more compact, hence suitable for large files.

By default, output will occur just once, after the entire session. But if you are using :ref:`time_feature` and wish to have separate output from specific runs::

    b:Sc/MyScorer/OutputAfterRun = "True" # set True to trigger output of scorer after this run
    # If this is always set False, or not defined, we just output at the end of the session.
    # If this is always set True, we output after every run.

Additional output control options::

    b:Sc/MyScorer/OutputToConsole = "True" # control whether output is also dumped to console
    s:Sc/MyScorer/IfOutputFileAlreadyExists = "Increment" # "Exit", "Overwrite" or "Increment"

We keep name and type separate in the above so that one can do things like change all output from csv to AIDA by just changing a single parameter (by setting many ``OutputType`` parameters equal to a common relative string paramater).
