Specialized Components
----------------------

=========================== ========================
:ref:`geometry_rmw`         "TsRangeModulator"
:ref:`geometry_propeller`   "TsPropeller"
:ref:`geometry_ridgefilter` "TsRidgeFilter"
:ref:`geometry_mwc`         "TsMultiWireChamber"
:ref:`geometry_mlc`         "TsMultiLeafCollimator"
:ref:`geometry_cad`         "TsCAD"
:ref:`geometry_aperture`    "TsAperture"
:ref:`geometry_compensator` "TsCompensator"
:ref:`geometry_dicom`       "TsDicomPatient"
:ref:`geometry_xio`         "TsXioPatient"
=========================== ========================

Each of the specialized components has its own set of special parameters. Usage is best learned by studying the examples parameter files included in TOPAS (see below).

You may write your own additional components (see Extending TOPAS at the end of this user guide).

The following figure from Samsung Medical Center shows how their very specific quadrupole magnet system was coded as a TOPAS geometry.

.. image:: SMC.png



.. _geometry_rmw:

Range Modulator Wheel
~~~~~~~~~~~~~~~~~~~~~

TOPAS Range modulator is designed to accommodate various specifications from a vendor. We suggest to create or model your Range Modulator Wheel (RMW) by following procedure:

* Define the dimension of RMW drum, such as thickness and material of shell and hub (see figure below). Tracks will be placed in between the hub and the shell.
* This space (in between hub and shell) is vertically divided into three sections named, "Upper", "Middle", and "Bottom" so that each section can have its own tracks. You can adjust heights of these sections. The sum of these heights is the total height of your RMW.
* In order to reserve spaces for tracks, divide radially each section into as many as tracks you want by using the parameter, "RadialDivision."
* Using vector parameters, configure the tracks individually such as each block’s height, span angle, and material. Then assign vector parameter to the parameter, called "Pattern."

.. image:: RMW_1.png

Illustration for TOPAS RM dimensions. Tracks are placed in between Rout of Hub and Rin of Shell and this area is to be radially divided in case of placing multiple tracks. There are three vertical rooms, so it is possible to make double sided RMWs with an interface disk.

.. image:: RMW_2.png

An example of RMW; (a) Perspective view. Upper section is divided into two but only inner radial division has a track pattern. In middle section, two track patterns are used to make a hole. (b) X-Y view from +z of RMW and (c) X-Y view from -z of RMW. Tracks are drawn in wireframe style, so more lines on the tracks are shown than the number of blocks.

Here is the complete set of the parameters for the above RMW (see :ref:`example_special_rmw` example)::

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

In same way, you can configure other tracks.
Then the track1 on upper area looks like following figure.

.. image:: RMW_3.png

A track pattern from the parameter above; (left) a complete set of the track view. (right) blocks are constructed in counterclockwise.

::

    b:Ge/RangeModulatorA/PrintInformation = "True" #Print out specification, see below

When TOPAS builds the geometry, you will see the numbers are input properly from console output as:

.. code-block:: text

    ---UpperTrack1 , # of Blocks: 14
    0th Block
      Angle : 5, 115 deg
      Height : 7.7 cm
      Material: Ts_Lexan
    1st Block
      Angle : 115, 146.5 deg
      Height : 8.2 cm
      Material: Ts_Lexan
    2nd Block
      Angle : 146.5, 173.2 deg
      Height : 8.7 cm
      Material: Ts_Lexan
    3rd Block
      Angle : 173.2, 195.07 deg
      Height : 9.215 cm
      Material: Ts_Lexan
    4th Block
      Angle : 195.07, 216.15 deg
      Height : 9.5 cm
      Material: Ts_Lexan
    ...

TOPAS RMW is a specialized geometry and so allows only the rotation around z-axis as well as the propeller rotation. Two examples demonstrate how to rotate RMW and modulate beam current (:ref:`example_special_rmw_constant` and :ref:`example_special_rmw_modulated`). The detail explanation for cooperating with Time Feature is followed later.


.. _geometry_propeller:

Propeller
~~~~~~~~~



.. _geometry_ridgefilter:

Ridge Filter
~~~~~~~~~~~~



.. _geometry_mwc:

Multi Wire Chamber
~~~~~~~~~~~~~~~~~~



.. _geometry_mlc:

Multi Leaf Collimator
~~~~~~~~~~~~~~~~~~~~~



.. _geometry_cad:

CAD (Computer Aided Design)
~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. _geometry_aperture:

Aperture
~~~~~~~~



.. _geometry_compensator:

Compensator
~~~~~~~~~~~



.. _geometry_dicom:

Patient in DICOM Format
~~~~~~~~~~~~~~~~~~~~~~~



.. _geometry_xio:

Patient in XiO Format
~~~~~~~~~~~~~~~~~~~~~





Hounsfield Conversion
~~~~~~~~~~~~~~~~~~~~~
