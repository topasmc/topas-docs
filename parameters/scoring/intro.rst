Introduction
------------

There are two basic classes of scorers: one class score activity in a volume (such as Energy or Dose), the other class score activity at a surface (such as Track Count or Phase Space).

Most scorers output overall quantities that are accumulated over many particles (counts and averages), but other scorers can output specific information per particle (in an n-tuple format).

You can have any number of scorers. A scorer is defined when you have a line that ends with Quantity, such as::

    s:Sc/MyScorer/Quantity = "DoseToMedium"

You may write your own additional scorers (see Extending TOPAS at the end of this user guide).
