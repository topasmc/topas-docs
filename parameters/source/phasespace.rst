.. _source_phasespace:

Phase Space Sources
-------------------

Phase Space refers to the technique of saving or replaying a set of particles crossing a given surface.

* When one saves a phase space, one defines a surface and then saves the position, particle type, energy and momentum of some or all particles crossing that surface.
* When one replays a phase space, one starts a set of particles from the saved positions, with the saved particle types, energy and momentum.

Phase Space enables separating two parts of a simulation or analysis job, and can be used to transfer sets of particles among different codes.

Each phase space must come as two related files (with same file name but different file extensions):

* A .header file tells the number of histories, the number of saved particles and the order of information in the .phsp file
* A .phsp file contains all the details of all the saved particles

We support three formats for Phase Space (and TOPAS automatically figures out the format of your .phsp file by studying the related .header file):

* ASCII provides particle information in a human-readable text file, which data encoded as a series of columns of text. The header file tells the contents and column order per particle.
* Binary provides the same information as ASCII, but in a much more compact format, with data encoded in a stream of bytes. The header file tells the contents and byte order per particle. Use Binary in cases where the ASCII format produces excessively large files.
* Limited is an alternate binary format compatible with some legacy codes. It has fewer options for what data can be expressed, but is compatible with codes such as that used by Varian for their TrueBeam phase space files. Use Limited format only when you need to exchange phase space with legacy codes.

Some users have found legacy phase space files that were unreadable in the Limited format because, though they were supposed to contain information about which particles represent a new history, there was in fact no new history information. In such cases, it seems that all photons were to be considered new histories. To read such files, use the Limited format with the additional TOPAS parameter::

   b:So/MyPhaseSpaceSource/LimitedAssumePhotonIsNewHistory = "true"

Note that while our Phase Space Scorer lets you also write phase space to `ROOT files <https://root.cern.ch>`_, we do not provide the capability read phase space back in from this format.
For more details, see :ref:`phasespace_format`.

Phase Space sources ignore the parameters starting with "Beam" and instead use::

    s:So/MySource/Type = "PhaseSpace"
    s:So/MySource/Component = "World" # coordinate system of phase space. Usually "World"
    s:So/MySource/PhaseSpaceFileName = "ASCIIOutput" # match exact case

TOPAS will look for header and phsp files with the given ``PhaseSpaceFileName``.

You can generate some sample data by running any of the examples: :ref:`example_phsp_ascii_write`, :ref:`example_phsp_binary_write` or :ref:`example_phsp_limited_write`.

When using phase space sources, it is important to decide how you want to handle a special case we call "Empty Histories." Recall that when a phase space is first recorded, for a given Original History, the set of resulting particles that cross the phase space surface:

* may include the primary particles, or
* may include a mix of primary and secondary particles, or
* may include only secondary particles, or
* may include no particles at all. We refer to this last case as an "Empty History."

When you subsequently use this file as a Phase Space Source, you need to decide how you want TOPAS to handle Empty Histories. If you're just calculating sums, it doesn't matter. The Empty Histories contribute nothing to the sum anyway. But if you're calculating statistical quantities, such as Mean, then these Empty Histories matter. Imagine you want to know the mean dose per Original History. If half of the Original Histories never made it to the phase space file, the decision of whether or not to include these Empty Histories will give a factor of two difference in the calculated Mean Dose per History.

Depending on your use case you may or may not want to include these Empty Histories. It comes down to whether the statistics you want to calculate are:

* per Original History, or
* per Original Histories that Reached Phase Space

You control this with::

    s:So/MySource/PhaseSpaceIncludeEmptyHistories = "False" # defaults to false

TOPAS ASCII and Binary phase space format headers show all of the relevant information:

* Number of Original Histories
* Number of Original Histories that Reached Phase Space
* Number of Scored Particles

Limited phase space format header does not give:

* Number of Original Histories that Reached Phase Space
* so the only way to get that in Limited format is to first read through the entire phsp file and count how many histories contributed there.

TOPAS provides an option to check that the values in the header match what is in the file::

    s:So/MySource/PhaseSpacePreCheck = "True" # defaults to true

For TOPAS ASCII and Binary formats, this is a thorough safety check. It will catch any cases where the files have somehow become corrupted (as could happen, for example, if you are doing a very long phase space writing job and the output disk becomes full during some part of the job).
For Limited format, the check is still helpful but less thorough as the header file provides incomplete information. In Limited format, if you want to include Empty Histories, the check is required as it is the only way TOPAS can figure out how many Empty Histories there were.

If the phase space you are replaying came from a TOPAS job, the particle starting positions in that file will have been defined relative to the ``World`` Component. Set the ``Component`` parameter above to ``"World"``. If you want to offset these particles to some other center or orientation, choose a Component that has the new desired center and orientation (reuse some existing Component, or define a new Group Component just for this purpose). If the phase space you are replaying did not come from TOPAS, there is no automatic way to know what coordinate system was used. It will be up to you to choose a Component that has this appropriate coordinate system.

You can optionally tell the phase space source to scale its position information::

    u:So/MySource/PhaseSpaceScaleXPosBy = 0.1 # adjust starting point on X axis by factor of 0.1
    u:So/MySource/PhaseSpaceScaleYPosBy = 0.1 # adjust starting point on Y axis by factor of 0.1
    u:So/MySource/PhaseSpaceScaleZPosBy = 0.1 # adjust starting point on Z axis by factor of 0.1
 
You can tell the phase space source to ignore parts of its position information by scaling by zero::

    u:So/MySource/PhaseSpaceScaleXPosBy = 0.
    u:So/MySource/PhaseSpaceScaleYPosBy = 0.
    u:So/MySource/PhaseSpaceScaleZPosBy = 0.

That coordinate of the particle position then just exactly matches the Component center.

You can optionally invert any of the phase space axes by::

    b:So/MySource/PhaseSpaceInvertXAxis = "True"
    b:So/MySource/PhaseSpaceInvertYAxis = "True"
    b:So/MySource/PhaseSpaceInvertZAxis = "True"

In most cases you will instead want to just rotate the source component. However if the handedness of your source phase space is incorrect, one of these invert options will be necessary.

By default, a PhaseSpace source will run all of the histories in the file. To run all of the histories multiple times::

    i:So/MySource/PhaseSpaceMultipleUse = 2 # reuse this phase space multiple times

If you set ``PhaseSpaceMultipleUse`` to zero, the number of histories in the file will be ignored, and we will instead run the exact number from::

    i:So/MySource/NumberOfHistoriesInRun

This may mean only partial use of the phase space file, or partial reuse to get the right number of histories.

* If your data was generated with time dependence, partial reuse of phase space may not give valid results (you may be playing back only a part of the time sequence). Many more details on controlling number of histories are found in :ref:`time_mode`.
* Partial reuse of phase space can not include Empty Histories. There is no statistically valid way to handle these empty histories when the phase space file is only partially used (since one does not know where in the phase space order these Empty Histories would have occurred).

For efficiency, the phase space file will be read in chunks of 10,000 particles at a time. Advanced users may find some reason to adjust this buffer size (though I can’t think of any)::

    i:So/MySource/PhaseSpaceBufferSize = 1000000

Take care when mixing Phase Space Sources with :ref:`time_feature`.
While TOPAS can save the current TOPAS time to a phase space file, this time is not automatically applied when reading particles back in from phase space. Thus, if you want to correctly replay source particles that were recorded with time features, it is your responsibility to apply the identical time features during the play back simulation. Some additional notes:

* Do not attempt to change the name of the phase space file over time. Save and replay all particles from a single phase space file.
* Do not use :ref:`time_mode_random`. The randomly generated times during playback will not necessarily match the randomly generated times that were saved to the phase space. Only use :ref:`time_mode_fixed` or :ref:`time_mode_sequential`.
* If your intention is to play back with exactly the same sequence as you had when you generated the phase space file, make sure to set::

    s:So/MySource/PhaseSpaceIncludeEmptyHistories = "True"

  otherwise empty histories will put the playback job out of synch with the original job.

A future version of TOPAS will provide more tools to synchronize and check playback time features.

.. todo:: Support time features with phasespace sources
