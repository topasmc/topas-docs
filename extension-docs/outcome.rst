.. _extension_outcome:

Custom Outcome Models
=====================

.. highlight:: c++

First line of the cc file must be of the form::

    // Outcome Model for MyOutcomeModel1

Your custom outcome model can perform whatever analysis you wish from a TOPAS DVH.
The work is all in your Initialize method.

See ExtensionsExamples/MyOutcomeModel1
