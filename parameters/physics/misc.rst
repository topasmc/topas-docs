Miscellaneous
-------------

User-Supplied Physics Lists
~~~~~~~~~~~~~~~~~~~~~~~~~~~

See :ref:`extension_physics` for details on how to provide your own physics list. This option is not recommended unless you have significant Geant4 expertise.



Multiple Physics Lists
~~~~~~~~~~~~~~~~~~~~~~

You can have more than one list defined at the same time, but only the one specified in ``Ph/ListName`` will actually be in effect::

    s:Ph/ListName = "MyList1"
    s:Ph/MyList1/Type= "QGSP_BERT_HP" # This list is in effect now
    d:Ph/MyList1/CutForAllParticles = 0.05 mm
    ...
    s:Ph/MyList2/Type= "Geant4_Modular" # This list goes into effect if Ph/ListName set to MyList2
    sv:Ph/MyList2/Modules = 1 "g4em-standard_opt3"
    d:Ph/MyList2/CutForGamma = 0.04 mm



Production Thresholds
~~~~~~~~~~~~~~~~~~~~~

Production Thresholds and range cuts are discussed in detail in the `Geant4 Application Developers Guide <http://geant4-userdoc.web.cern.ch/geant4-userdoc/UsersGuides/ForApplicationDeveloper/html/TrackingAndPhysics/thresholdVScut.html>`_. By default, appropriate limits are set by the physics list. You can override these defaults with::

    d:Ph/MyPhysics/SetProductionCutLowerEdge = 200 eV
    d:Ph/MyPhysics/SetProductionCutHighEdge = 30 MeV



Step Size
~~~~~~~~~

The selection of step size is a complex issue in Monte Carlo tracking. Geant4 has its own complex logic for automatically selecting what it thinks will be an appropriate step size, based on local geometry and physics, and the user will not generally need to override this automatic behavior. However, your applications may be sensitive to this behavior, and you may therefore want to set a maximum step size in certain components. In general, larger step sizes give faster performance, but smaller step sizes may give better accuracy.

To limit Geant4's maximum step size in a given component::

    d:Ge/MyComponent/MaxStepSize = 1. mm # sets maximum step size used in this component

Step size settings do not affect other Components placed within this Component. You must explicitly set the step size for any subcomponents that you want to affect.

The choice of maximum step size is highly dependent on your exact simulation problem. If you think you need to set a maximum step size, try running with several values, and pick one for which a small variation up or down does not cause a significant change in results.
