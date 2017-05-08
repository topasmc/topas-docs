.. _extension_scoring:

Custom Scorers
==============

.. highlight:: c++

First line of the cc file must be of the form::

    // Scorer for MyScorer1

Your custom scorer can either accumulate binned data (like our built-in dose scorer), or n-tuple data (like our built-in phase space scorer).

* For binned scorers, your scorer should inherit from TsVBinnedScorer.
* For n-tuple scorers, your scorer should inherit from TsVNtupleScorer.

At a minimum, your scorer should provide a constructor, a destructor and a ProcessHits method. The base class will take care of all the details of filtering, accumulating and outputting results.

For binned scorers, your scorer's constructor must contain a call to::

    SetUnits

For n-tuple scorers, your scorer's constructor defines each column and its data type by calls to::

    RegisterColumnD
    RegisterColumnF
    RegisterColumnI
    RegisterColumnI8
    RegisterColumnB
    RegisterColumnS

RegisterColumnD and RegisterColumnF also take a unit string.

If your scorer is a Surface Scorer, the constructor must also contain the line::

    SetSurfaceScorer();

Otherwise, your scorer is assumed to be a Volume Scorer.

The scorer’s ProcessHits method must be written carefully to avoid slowing down the simulation since this method is called for every hit in the scoring component. Slow operations such as string comparisons should be avoided here. Try to write your code so that you perform these sorts of slow operations only during construction, save values and pointers in class variables and then use these pre-calculated values in the ProcessHits method. Once you have your value computed:

* For binned scorers, accumulate data by calling ``AccumulateHit``
* For n-tuple scorers, accumulate data by calling ``fNtuple->Fill``

If you want to take more complete control of the scoring process, you can provide optional methods::

    // called after the last hit of a given track
    void UserHookForEndOfTrack()
    // called after the last hit of all tracks resulting from a given particle incident on the scoring component
    void UserHookForEndOfIncidentParticle()
    // called at the end of the event
    void UserHookForEndOfEvent()
    // called at the end of the run
    void UserHookForEndOfRun()

Between the ProcessHits method and these other four methods, you have complete control over how you will accumulate and handle your scored values. Accumulate values in your own data structures that you provide in your scorer’s header file or in other classes that your scorer calls. Manipulate and output these values as you wish. It is all up to you. You can still choose to fill the fEvtMap just like a regular scorer, in which case TOPAS will accumulate and output those values, or you can fill nothing into that fEvtMap, in which case TOPAS will not take any further action for this scorer.

Some helper functions you may want to use from the TsParameterManager::

    // Activates creation of the TsTrackInformation object
    SetNeedsTrackingAction
    // Activates creation of the extra part of the TsTrackInformation object that contains information on what volumes were traversed
    SetNeedsSteppingAction

Some helper functions you may want to use from the TsVScorer::

    // Get pointer to a material
    GetMaterial
    // Tell whether a given material is used in the geometry
    UsedMaterial
    // Get the voxel index from hits in divided or parameterized components
    GetIndex
    // Get the current TOPAS time (for the time of flight, use fTimeOfFlight)
    GetTime
    GetRunID
    GetEventID
    GetRandomNumberStatusForThisEvent
    // Disable the automatic creation and filling of output, leaving this work entirely to your scorer
    SuppressStandardOutputHandling

For divided components, the combined index one finds in scorers is formed from three bin indices (x,y,z or r, phi, z or r, phi, theta for TsBox, TsCylinder and TsSphere respectively). A helper function is now provided to return the individual bin indices given the combined index::

    GetBin(index, iBin) // where iBin is 0, 1 or 2

A scorer can itself instantiate additional scorers. We refer to these as "SubScorers".
The main scorer can then perform calculations using results of one or more  subscorers to obtain a final value.
A good example of this is in ExtensionExamplesMore/MyScoreProtonLET.
At the end of the constructor, it contains the following::

	InstantiateSubScorer("ProtonLET_Denominator", outFileName, "Denominator");

And later there is a method that combines the scorer and the subscorer on a bin-by-bin basis to obtain a final quantity per bin::

    G4int MyScoreProtonLET::CombineSubScorers()
    ...
	fFirstMomentMap[index] = fFirstMomentMap[index] / denomScorer->fFirstMomentMap[index];
