.. _time_feature:

Time Features
=============

While the repeatability requirements of the TOPAS parameter system require that parameter definitions be well specified, there is still a need to define time-dependent behaviors (such as motion, beam current modulation, starting and stopping of scoring activities). The TOPAS Time Feature system allows such time-dependence to be specified in a manner that is both flexible and repeatable.

A Time Feature is a set of parameters that ultimately describes the change of a time feature ``Value``. You provide parameters that define the time function, such as a linear change over time.
TOPAS automatically creates a ``Value`` parameter for this function (a parameter you don’t define). TOPAS continually updates this ``Value`` parameter to the appropriate value for a given time.

.. note::

    If you're doing complex things with parameter file chains, you may want to know where in chain this automatically added ``Tf/.../Value`` parameter goes: the answer is that it goes into the same virtual file as the ``Tf/.../Function`` parameter.

In addition to specifying the time features, you need to specify the overall time sequence for :ref:`time_mode_sequential`.



**First example**

Here is an example, a Time Feature called ``ArmRot`` that describes a constant rotation::

    s:Tf/ArmRot/Function = "Linear deg"
    d:Tf/ArmRot/Rate = 2. deg/ms
    d:Tf/ArmRot/StartValue = 0.0 deg
    d:Tf/ArmRot/RepetitionInterval = 50. ms

TOPAS automatically creates another parameter::

    s:Tf/ArmRot/Value

and updates this parameter to the appropriate value for a given time.

You can then use this value to affect a component position through a statement such as::

    d:Ge/Arm/RotX = 0. deg + Tf/ArmRot/Value



Linear, Sine, Cosine and Sqrt Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For **Dimensioned Double or Unitless** values, the ``Function`` can be any one of:

=========   ====================================
Function    Value(Time)
=========   ====================================
Linear      StartValue + Rate * Time
Sine        Sine ( StartValue + Rate * Time )
Cosine      Cosine ( StartValue + Rate * Time )
Sqrt        Sqrt ( StartValue + Rate * Time )
=========   ====================================

If the value is Dimensioned Double, you must also provide a unit, such as the ``deg`` in::

    s:Tf/ArmRot/Function = "Linear deg"

You must provide appropriate ``StartValue`` and ``Rate`` parameters, such as::

    d:Tf/ArmRot/Rate = 2. deg/ms
    d:Tf/ArmRot/StartValue = 0.0 deg

``RepetitionInterval``, is the time interval after which the function will reset to the ``StartValue``. If you do not provide this parameter, the function will not reset.



Step Function
~~~~~~~~~~~~~

With a Step function, you can control **any** type of parameter value. You define a set of times at which to change value, and a value for each of those times. The first value you provide specifies the starting value (the value at time zero).

Here is an example of a Step time feature that controls a String::

    s:Tf/ImageName/Function = "Step"
    dv:Tf/ImageName/Times = 3 10 20 30 ms
    sv:Tf/ImageName/Values = 3 "lung-1" "lung-2" "lung-3"

* The first value is used for times ``Tf/TimelineStart`` to 10 ms.
* If ``Tf/TimelineStart`` was not specified, it defaults to 0, so that first value will be used for times 0 to 10 ms.
* The second value is used for times 10 to 20 ms.
* The third value is used for times 20 to 30 ms.
* After 30 ms, the value cycles back to the first value.

Note that the first member of Values is not the time that the first Value should be used.
It is the time that the first Change of value should be made.
The first Value will be used for the time between ``Tf/TimelineStart`` and that first member of Tf/*/Times.

Note that whereas continuous functions (Linear, Sine, Cosine and Sqrt) include a ``RepetitionInterval``, Step Functions do not. They just cycle back to the first ``Value`` after the last of the ``Times`` is reached.

Here is an example of a Step time feature that controls a Boolean::

    s:Tf/ScoringOnOff/Function="Step"
    dv:Tf/ScoringOnOff/Times =10 10 20 30 40 50 60 70 80 90 100 ms
    bv:Tf/ScoringOnOff/Values=10 "true" "false" "true" "false" "false" "true" "true" "true" "false" "true"

Note that:

* ``Tf/.../Times`` is always of type ``dv:`` and has unit of time.
* ``Tf/.../Values`` is a vector of whatever type the function controls.

Any individual member of the ``Values`` parameter vector can itself be a parameter, such as::

    bv:Tf/ScoringOnOff/Values=4 "true" "false" Some_Other_Boolean_Parameter_Name "false"



Combining Time Features for Complex Behaviors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can add or multiply time feature ``Value`` parameters just as you can add or multiply any other kind of parameter. For example, here is how the number of histories in a run can be controlled by both a beam current and a beam weight::

    s:Tf/BeamCurrent/Function = "Step"
    dv:Tf/BeamCurrent/Times = 1 10 ms
    iv:Tf/BeamCurrent/Values = 1 10

    s:Tf/BeamWeight/Function = "Step"
    dv:Tf/BeamWeight/Times = 10 1 2 3 4 5 6 7 8 9 10 ms
    iv:Tf/BeamWeight/Values = 10 1 1 1 2 2 2 2 4 4 4

    i:Tf/BCM/Value = Tf/BeamWeight/Value * Tf/BeamCurrent/Value
    i:So/MySource/NumberOfHistoriesInRun = Tf/BCM/Value

By combining Step time features with other time features, you can control complex sequences.
The following from :ref:`example_special_purgingmagnet` moves a box first in one direction and then in the other::

    s:Tf/BackForward/Function = "Step"
    dv:Tf/BackForward/Times = 2 100.0 200.0 ms
    dv:Tf/BackForward/Values = 2 Tf/BackStep/Value Tf/ForwardStep/Value mm

    s:Tf/BackStep/Function = "Linear mm"
    d:Tf/BackStep/Rate = 3 mm/ms
    d:Tf/BackStep/StartValue = 0.0 mm
    d:Tf/BackStep/RepetitionInterval = 100.0 ms

    s:Tf/ForwardStep/Function = "Linear mm"
    d:Tf/ForwardStep/Rate = -3 mm/ms
    d:Tf/ForwardStep/StartValue = 300.0 mm
    d:Tf/ForwardStep/RepetitionInterval = 100.0 ms

Some complex examples of time features are in examples/Nozzle.
While we have had examples of double scattering and pencil beam scanning for some time, those examples have included proprietary IBA information, so could not be generally shared. The examples found in examples/Nozzle have no vendor confidential information.

=========================================   =====================================
Example                                     Description
=========================================   =====================================
:ref:`example_nozzle_raster`                Time Features for controlling the dipole magnets are implemented. The time varying magnet will scan rectangle fields in a raster pattern.
:ref:`example_nozzle_scanning_stationary`   In addition to RasterScanningPattern.txt, a water phantom including a plane target is added.
:ref:`example_nozzle_scanning_horiz`        The perpendicularly moving target is defined. In order to make protons follow the moving target, compensated Time Features for the dipole magnets are implemented. The execution of this file will show the moving target in horizontal direction and the proton beams tracking the moving target.
:ref:`example_nozzle_scanning_depth`        To trace the target moving along with the depth, the changes of proton’s incident energy should be synchronized with the motion.
:ref:`example_nozzle_scanning`              All geometry for the scanning nozzle is defined. The nozzle consists of magnet systems, for example, two quadrupole magnets and two dipole magnets in helium gas filled beam pipe and various monitoring chambers. Magnet fields are set to zero in this parameter file.
:ref:`example_nozzle_scattering`            All geometry for the scattering nozzle is defined.
:ref:`example_nozzle_scattering_run`        Range Modulator Wheel rotates over time and scatterers move in and out of the beam.
=========================================   =====================================

.. warning::

    Take care when mixing Phase Space Sources with Time Features.
    While TOPAS can save the current TOPAS time to a phase space file, this time is not automatically applied when reading particles back in from phase space. Thus, if you want to correct replay source particles that were recorded with time features, it is your responsibility to apply the identical time features during the play back simulation. Some additional notes:

    * Do not attempt to change the name of the phase space file over time. Save and replay all particles from a single phase space file.
    * Do not use :ref:`time_mode_random`. The randomly generated times during playback will not necessarily match the randomly generated times that were saved to the phase space. Only use :ref:`time_mode_fixed` or :ref:`time_mode_sequential`.

    A future version of TOPAS will provide more tools to synchronize and check playback time features.

.. todo:: Readback time from phasespace
