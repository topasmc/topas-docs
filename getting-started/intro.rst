Introduction to TOPAS
=====================

TOPAS_ wraps and extends the `Geant4 Simulation Toolkit`_ to provide an easier-to-use application for the medical physicist. TOPAS's unique parameter control system lets you assemble and control a rich library of simulation objects (geometry components, particle sources, scorers, etc.) with no need to write C++ code.

Advanced users remain free to implement their own simulation objects in C++ code, and add them to TOPAS via an :ref:`extension mechanism <extensions>`. While user-written objects benefit from underlying functionality of TOPAS base classes and the TOPAS parameter system, they can exploit the full flexibility of Geant4.

.. note:: Users should carefully read the :ref:`parameters_intro`, as well as the introductory parts of the sections :ref:`geometry`, :ref:`source`, :ref:`physics` and :ref:`scoring`). The rest of the documentation provides a detailed reference that you may just want to skim initially.


.. _TOPAS: http://www.topasmc.org
.. _Geant4 Simulation Toolkit: https://geant4.web.cern.ch
