.. _parameters_relative:

Relative Parameters
-------------------

TOPAS supports "relative parameters", wherein one parameter may be set relative to another, as in::

    s:Ge/Phantom/Material = SomeOtherParameterName

.. note::

    The many uses of this relative parameter syntax become more clear once one understands the entirety of the TOPAS design, including :ref:`hierarchical control <parameters_hierarchy>` files and :ref:`time features <time_feature>`.

With relative dimensioned double parameters, we must protect against a user setting a parameter relative to some other parameter that does not have appropriate units. The solution is to insist that a unit be included on the right side of the expression. In the example below, the unit of ``cm`` indicates that SomeOtherParameter must itself have units of length. If that other parameter’s unit is of the entirely wrong unit category (mass, angle, etc.), TOPAS will refuse to run. If the unit is of the right category but a different exact unit (m, mm, etc.), TOPAS will perform appropriate unit conversion::

    d:Ge/Phantom/HLX = SomeOtherParameterName cm

TOPAS has a grammar for operations such as adding or multiplying parameters::

    Ge/Compensator/TransZ = Ge/Aperture/DistalEdge + Ge/Compensator/HLZ mm

.. warning::

    Note that there must be a space before and after the plus sign.

Relative parameters allow only a limited number of functions, intentionally not a full math library, since other math functions may be ambiguous, requiring too much prior understanding of the mathematical syntax. The complete set of allowed syntax for any one parameter line is shown :ref:`here <parameters_syntax_all>`.
