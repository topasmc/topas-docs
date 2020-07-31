Introduction
------------

In Geant4, physics options are set in pieces of code called "Physics Lists". A physics list specifies what particles and physics processes are defined, plus various cuts and options.
By default, we set TOPAS physics to a list that has been shown to work well for proton therapy research at the Massachusetts General Hospital. This list includes models that handle not only protons but also all secondary particles (neutrons, helium ions, deuterons, tritons, photons, electrons, etc.). The default gives results that closely match a previous custom list that was described in:

* C. Zacharatou Jarlskog and H. Paganetti, "Physics settings for using the Geant4 toolkit in proton therapy," IEEE Trans. Nucl. Sci. 55, 1018-1025 (2008)

but which can no longer be used since that list corresponded to a much earlier Geant4 release.

The choice of physics list generally depends on the accuracy required for the scored quantities and the speed of the calculation. The Geant4 Medical Simulation Benchmark Group (G4MSBG) has collected a comprehensive set of mainly measured benchmarks that are run at the time of each Geant4 release. Results may be viewed at https://geant-val.cern.ch/ (see Arce et al, “Report on G4-Med, a Geant4 benchmarking system for medical physics applications developed by the Geant4 Medical Physics Benchmarking Group,” In press, Med Phys, April 2020). Future benchmarks will include the trade-off with speed. 

Advanced users can set their own parameters to override some of these default settings, or can specify entirely different physics lists.

You can choose from two general types of physics lists:

* :ref:`physics_reference` are pre-made, complete lists provided by Geant4.
* :ref:`physics_modular` are lists where you mix and match a set of modules to create a customized complete list.

You can also provide your own physics list using :ref:`extension_physics` (not recommended unless you have significant Geant4 expertise).

You can get a list of what processes are in your currently selected physics list by::

    b:Ph/ListProcesses = "True"
