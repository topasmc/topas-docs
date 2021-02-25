Introduction
------------

There are two basic classes of scorers:

* :ref:`scoring_volume` (e.g. Energy or Dose)
* :ref:`scoring_surface` (e.g. Track Count or Phase Space)

Most scorers output overall quantities that are accumulated over many particles (counts and averages), but other scorers can output specific information per particle (in an n-tuple format).

You can have any number of scorers. A scorer is defined when you have a line that ends with ``Quantity``, such as::

    s:Sc/MyScorer/Quantity = "DoseToMedium"

When your scoring component is the Parent of other components, you have the option to set scoring to record particles not only in the parent component, but also in its children.

    b:Sc/MyScorer/PropagateToChildren = "True"

This action is recursive to all levels of subcomponents.

You may write your own additional scorers (see :ref:`extension_scoring`).
