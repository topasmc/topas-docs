.. _extension_filter:

Custom Filters
==============

.. highlight:: c++

First line of the cc file must be of the form::

    // Filter for OnlyIncludeParticlesOfTwiceAtomicNumber,OnlyIncludeParticlesNotOfTwiceAtomicNumber

Note that a single filter can be used for more than one filter condition, hence comma separated list.

Filters must be written carefully to avoid slowing down the simulation. The filter’s Accept method is called for every hit in the scoring component. Slow operations such as string comparisons should be avoided during this method. Try to write your code so that you perform these sorts of slow operations only during the constructor, ResolveParameters method or CacheGeometryPointers method, save values and pointers in class variables and then use these pre-calculated values in the ProcessHits method.

Parameter lookups should be done in ResolveParameters. Call ResolveParameters directly from your constructor, and then you can also rely on TOPAS to re-call this method any time one of this filter’s parameters is changed.

4D behaviors may require TOPAS to destroy and rebuild components during the simulation. Accordingly, you can not rely on the pointer to a given component remaining the same throughout the simulation. Any lookup of a component pointer should be done in the filter’s CacheGeometryPointers method. TOPAS will re-call this method any time relevant components are rebuilt.

Some helper functions you may want to use from the TsParameterManager::

    // Activates creation of the TsTrackInformation object
    SetNeedsTrackingAction
    // Activates creation of the extra part of the TsTrackInformation object that contains information on what volumes were traversed
    SetNeedsSteppingAction

Some helper functions you may want to use from the TsVFilter::

    // Get pointer to a material
    GetMaterial
    // Get pointer to a named physics volume
    GetPhysicalVolume
    // Get pointer to a named component
    GetComponent
    // Get pointers to all children of a named component
    GetChildComponentsOf

