.. _extension_source:

Custom Particle Sources
=======================

.. highlight:: c++

First line of the cc file must be of the form::

    // Particle Source for MyParticleSource1
    or
    // Particle Generator for MyParticleGenerator1

Your particle source defines the initial particles that are then transported by the simulation.
Because Geant4's multi-threaded capability keeps part of this functionality in the master thread and other parts in the worker threads, you actually create two separate classes to create a particle source.

For the part of the source that controls overall behavior (usually just setting the number of histories, but optionally also things like reading in some kind of phase space file), you write a class derived from TsSource. TOPAS instantiates this in the Geant4 Master thread. If you really just need this class to set the number of histories, you may just use our existing TsSource (that is, you don't have to write your own class at all for this part).

For the part of the source that generates the individual events (setting the primary particle positions and momenta), you write a class derived from TsVGenerator. TOPAS instantiates this in the Geant4 worker thread.

In both cases, parameter lookups should be done in ResolveParameters. Call ResolveParameters directly from your constructor, and then you can also rely on TOPAS to re-call this method any time one of this particle source's parameters is changed.

TOPAS will call your GeneratePrimaries method once per history. You should always start this method with this test::

    if (CurrentSourceHasGeneratedEnough()) return;

This allows your source to properly coexist with other sources that may have other numbers of histories.

The body of your GeneratePrimaries method should create and fill some number of TsPrimaryParticles (a single history may contain zero, one or more primary particles).

The TsPrimaryParticle structure is defined in the header file TsVParticleSource.hh. For each TsPrimaryParticle that you define, call GenerateOnePrimary.

Once you have finished creating all of the TsPrimaryParticles for this history, call AddPrimariesToEvent.
