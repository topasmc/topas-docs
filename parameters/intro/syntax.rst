.. _parameters_syntax:

Syntax
------

The TOPAS Parameter System is a control structure for applications in which a large number of complex inter-related parameters must be controllable by designers and end-users in a manner that is absolutely flexible but simultaneously easy to use. The system is designed with safety and repeatability as top priorities. A key error-checking strategy is strict type checking, in which every parameter must have a specific declared type (string, boolean, integer, etc.) and the provided values are checked to make sure they are appropriate to the given type.

The system takes a set of "Parameters Files," simple text files made up of lines of key/value pairs::

    Parameter_Type : Parameter_Name = Parameter_Value # Optional comment

When you edit parameter files, be careful to use a Plain Text editor. TOPAS will not understand the various hidden characters created by complex word processors (such as Word or Keynote). Whatever your editor, turn off advanced features such as "Smart quotes", "Smart dashes" and "Smart links".

Ten example parameter settings are given below::

    d:Ge/Phantom/HLX                           = 10. cm     # Dimensioned Double
    u:Ge/Magnet/Dipole/MagneticFieldDirectionX = 1.0        # Unitless Double
    i:Sc/DoseScorer/ZBins                      = 100        # Integer
    b:Sc/DoseScorer/Active                     = "True"     # Boolean
    s:Ge/Phantom/Material                      = "G4_WATER" # String
    dv:Ge/RMW_Track1/Angles         = 4 69.1 92.2 111.0 126.0 deg      # Dimensioned Double Vector
    uv:Ma/Phantom_Plastic/Fractions = 3 0.05549 0.75575 0.18875        # Unitless Double Vector
    iv:Gr/Color/yellow              = 3 225 255 0                      # Integer Vector
    bv:Tf/ScoringOnOff/Values       = 4 "true" "false" "true" "false"  # Boolean Vector
    sv:Ma/MyPlastic/Components      = 3 "Hydrogen" "Carbon" "Oxygen"   # String Vector

The order of lines within a parameter file does not matter.

A Parameter_Name can be almost any string, but we have prefix conventions to keep things clear:

* ``Ma/`` for Materials
* ``El/`` for Elements
* ``Is/`` for Isotopes
* ``Ge/`` for Geometry Components
* ``So/`` for Particle Sources
* ``Ph/`` for Physics
* ``Vr/`` for Variance Reduction
* ``Sc/`` for Scoring
* ``Gr/`` for Graphics
* ``Tf/`` for Time Features
* ``Ts/`` for TOPAS overall control

The Parameter_Type tells TOPAS what type of data will be in this parameter:

* ``d`` for Dimensioned Double
* ``u`` for Unitless Double
* ``i`` for Integer
* ``b`` for Boolean
* ``s`` for String
* ``dv`` for Dimensioned Double Vector
* etc. for ``uv``, ``iv``, ``bv`` and ``sv``

The only forbidden characters in a parameter name are: ``= + - * " ‘ ` TAB NEWLINE`` and ``RETURN``
The only forbidden characters in a parameter value are: = ``‘ ```

TOPAS uses this Parameter_Type to perform "strict type checking," checking that the Parameter_Value is appropriate and complete for the given Parameter_Type.

A String parameter must be in quotes and may take any value.

A Boolean parameter must be in quotes and may be either:

* ``"True"``, ``"t"`` or ``"1"`` (in any case) to mean true
* ``"False"``, ``"f"`` or ``"0"`` (in any case) to mean false

An Integer parameter must be something that can be interpreted as an integer.

* The value may not contain any decimal part, as this can lead to ambiguity as to the employed rounding strategy.
* These are 32 bit integers, thus the values can range from 0 to 2147483647.

A Dimensioned Double parameter requires both a value and a unit.

* We require the unit to avoid misunderstandings.
* The value must be something that can be interpreted as a floating point number.

A Vector of Dimensioned Doubles parameter requires an integer (larger than zero) to indicate how many values are expected, then the values themselves, then a unit.

* Vector of Dimensioned Doubles is useful when the definition of a single shape, motion, etc. requires multiple dimensioned double values.
* Our usage of the term "vector" may be unfamiliar to some readers but is the standard term for such structures in modern programming languages.

Vectors of Unitless, Integer, Boolean and String again require an integer to indicate how many values are expected, then the values themselves. The individual strings in a Vector of Strings can not contain spaces (this requirement will be relaxed in a subsequent TOPAS release).

The comment character is ``#``.
Anything to the right of the comment character is taken as a comment.
Comments can span as many lines as desired, until a new line is found that contains the equals sign.

A given parameter name may not be defined more than once in a single file.

Blank lines are ignored.

Parameter names may use mixed case, but their interpretation is not case sensitive.
That is, ``"myParameter"`` is considered the same as ``"myparameter"`` or ``"myPaRaMeter"``, etc.




Complete Set of Allowed Syntax for any one Parameter Line
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Note that in all of the expressions below, there must be a space before and after any ``+``, ``-`` or ``*``.

Dimensioned Double parameters::

    d:parameterName = number unit
    d:parameterName = number unit + name_of_dimensioned_double_parameter
    d:parameterName = number unit - name_of_dimensioned_double_parameter
    d:parameterName = number unit * name_of_unitless_or_integer_parameter
    d:parameterName = number * name_of_dimensioned_double_parameter unit
    d:parameterName = name_of_dimensioned_double_parameter unit
    d:parameterName = name_of_dimensioned_double_parameter unit * number
    d:parameterName = name_of_dimensioned_double_parameter unit * name_of_unitless_or_integer_parameter
    d:parameterName = name_of_unitless_or_integer_parameter * number unit
    d:parameterName = name_of_dimensioned_double_parameter + number unit
    d:parameterName = name_of_dimensioned_double_parameter - number unit
    d:parameterName = name_of_dimensioned_double_parameter + name_of_dimensioned_double_parameter unit
    d:parameterName = name_of_dimensioned_double_parameter - name_of_dimensioned_double_parameter unit

Unitless parameters::

    u:parameterName = number
    u:parameterName = number + name_of_unitless_or_integer_parameter
    u:parameterName = number - name_of_unitless_or_integer_parameter
    u:parameterName = number * name_of_unitless_or_integer_parameter
    u:parameterName = name_of_unitless_or_integer_parameter
    u:parameterName = name_of_unitless_or_integer_parameter + number
    u:parameterName = name_of_unitless_or_integer_parameter - number
    u:parameterName = name_of_unitless_or_integer_parameter * number
    u:parameterName = name_of_unitless_or_integer_parameter + name_of_unitless_or_integer_parameter
    u:parameterName = name_of_unitless_or_integer_parameter - name_of_unitless_or_integer_parameter
    u:parameterName = name_of_unitless_or_integer_parameter * name_of_unitless_or_integer_parameter

Integer parameters::

    i:parameterName = integer
    i:parameterName = integer + name_of_integer_parameter
    i:parameterName = integer - name_of_integer_parameter
    i:parameterName = integer * name_of_integer_parameter
    i:parameterName = name_of_integer_parameter
    i:parameterName = name_of_integer_parameter + integer
    i:parameterName = name_of_integer_parameter - integer
    i:parameterName = name_of_integer_parameter * integer
    i:parameterName = name_of_integer_parameter + name_of_integer_parameter
    i:parameterName = name_of_integer_parameter - name_of_integer_parameter
    i:parameterName = name_of_integer_parameter * name_of_integer_parameter

Boolean parameters::

    b:parameterName = value
    b:parameterName = name_of_boolean_parameter
    b:parameterName = name_of_boolean_parameter * name_of_boolean_parameter

String parameters::

    s:parameterName = string
    s:parameterName = string + name_of_integer_or_string_parameter
    s:parameterName = name_of_integer_or_string_parameter
    s:parameterName = name_of_integer_or_string_parameter + string
    s:parameterName = name_of_integer_or_string_parameter + name_of_integer_or_string_parameter

Dimensioned Double Vector parameters::

    dv:parameterName = number_of_values value1 value2 ... valueN unit
    dv:parameterName = number_of_values value1 value2 ... valueN unit + name_of_dimensioned_double_or_double_vector_parameter
    dv:parameterName = number_of_values value1 value2 ... valueN unit - name_of_dimensioned_double_or_double_vector_parameter
    dv:parameterName = number_of_values value1 value2 ... valueN unit * name_of_unitless_or_integer_or_unitless_vector_or_integer_vector
    dv:parameterName = number_of_values value1 value2 ... valueN * name_of_dimensioned_double_or_double_vector_parameter unit
    dv:parameterName = name_of_dimensioned_double_vector_parameter unit
    dv:parameterName = number * name_of_dimensioned_double_vector_parameter unit
    dv:parameterName = name_of_unitless_or_integer_parameter * name_of_dimensioned_double_vector_parameter unit
    # value1, value2, etc. can be a numeric value or the name of a dimensioned double parameter.

Unitless Vector parameters::

    uv:parameterName = number_of_values value1 value2 ... valueN
    uv:parameterName = number_of_values value1 value2 ... valueN + name_of_unitless_or_integer_or_unitless_vector_or_integer_vector
    uv:parameterName = number_of_values value1 value2 ... valueN - name_of_unitless_or_integer_or_unitless_vector_or_integer_vector
    uv:parameterName = number_of_values value1 value2 ... valueN * name_of_unitless_or_integer_or_unitless_vector_or_integer_vector
    uv:parameterName = name_of_unitless_vector_parameter
    uv:parameterName = number * name_of_unitless_vector_parameter
    uv:parameterName = name_of_unitless_or_integer_parameter * name_of_unitless_vector_parameter
    # value1, value2, etc. can be a numeric value or the name of a unitless parameter

Integer Vector parameters::

    iv:parameterName = number_of_values value1 value2 ... valueN
    iv:parameterName = number_of_values value1 value2 ... valueN + name_of_integer_or_integer_vector_parameter
    iv:parameterName = number_of_values value1 value2 ... valueN - name_of_integer_or_integer_vector_parameter
    iv:parameterName = number_of_values value1 value2 ... valueN * name_of_integer_or_integer_vector_parameter
    iv:parameterName = name_of_integer_vector_parameter
    iv:parameterName = integer * name_of_integer_vector_parameter
    iv:parameterName = name_of_integer_parameter * name_of_integer_vector_parameter
    # value1, value2, etc. can be a numeric value or the name of an integer parameter

Boolean Vector parameters::

    bv:parameterName = number_of_values value1 value2 ... valueN
    bv:parameterName = name_of_boolean_vector_parameter
    # value1, value2, etc. can be a numeric value or the name of a boolean parameter

String Vector parameters::

    sv:parameterName = number_of_values value1 value2 ... valueN
    sv:parameterName = number_of_values value1 value2 ... valueN + name_of_integer_or_string_or_integer_vector_or_string_vector
    sv:parameterName = name_of_string_vector_parameter
    # value1, value2, etc. can be a numeric value or the name of a string parameter

Other operations are intentionally not supported since their behavior might be unclear. Such things can be done in user C++ code, generating new parameters on the fly (see later discussion of "Transient Parameters"). ``d * d`` is forbidden because can create new units that we don't recognize. Division is forbidden because of divide by zero issues. etc.
