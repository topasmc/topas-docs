.. _parameters_optimization:

Parameter Optimization
======================

Any parameter (or set of parameters) in a topas simulation can be subject to formal mathematical optimisation according to a user-defined objective function using the third party library `TopasOpt <https://github.com/ACRF-Image-X-Institute/TopasOpt>`_. Some examples of situations where you may wish to optimize parameters include:

- you have some measured data and you wish to tune some parameters model to best match the measurement
- you are trying to speed up your topas runs and you want to optimise the physics settings to achieve faster runs with minimal change to simulation results
- you are trying to design a new device and want to maximize some performance criteria.

To get started with TopasOpt, start with the `worked examples <https://acrf-image-x-institute.github.io/TopasOpt/>`_

.. image:: BasicOptLoop.svg
  :alt: Basic Optimisation Loop