Introduction
------------

Variance, or noise, is in inherent property of Monte Carlo Method which decreases as more particles are run. As such, there is always a trade off between variance and simulation time.
Variance reduction techniques aim to shift this balance such that variance can be reduced without increasing simulation time. There are a number of ways you can think of doing this, for example:

- Bias certain interactions so they occur more often
- At a certain point, split certain particles N times, and reduce the weight of each particle by a factor of N
- Make some rules about which particles you care about, and kill the others

Note that some of these techniques only change the variance of the simulation, whereas others (like killing particles) will also change the *results* of your simulation. That can be ok if the result are changed in a region you don't care about, but obviously you have to be very careful. In general, the use of these techniques comes with a warning:

.. warning::
  Variance reduction (VR) techniques in TOPAS can be combined to create a very sophisticated setup. However, please note that VR is highly dependent on your specific geometry. Approach these features with caution and test all variance reduced setups against an equivalent setup without variance reduction. You should also review the Geant4 document that describes which cases are problematic `here <https://geant4.web.cern.ch/geant4/collaboration/working_groups/geometry/biasing/BiasScoreUseCases.html>`_.

To put this another way: ***with great power comes great responsibility.***

All variance reduction techniques in topas can be switched on/off with a master parameter::

    b:Vr/UseVarianceReduction = "true"

Specific variance reduction techniques are described next.
