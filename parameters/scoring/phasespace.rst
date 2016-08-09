Phase Space Output
------------------

Phase Space refers to the technique of saving or replaying a set of particles crossing a given surface. It is the only one of our built-in scorers that saves data to n-tuple format, rather than storing accumulated overall data (counts or averages). However you can write extension scorers to use this generalized n-tuple capability to store other information on a per-particle basis (see Extending TOPAS at the end of this user guide).

* When one saves a phase space, one defines a surface and then saves the position, particle type, energy and momentum of some or all particles crossing that surface.
* When one replays a phase space, one starts a set of particles from the saved positions, with the saved particle types, energy and momentum.

Phase Space enables separating two parts of a simulation or analysis job, and can be used to transfer sets of particles among different codes.

If your Surface Scorer has ``Quantity = "PhaseSpace"``, the output will be a pair of Phase Space files:

* A .header file tells the number of histories, the number of saved particles and the order of information in the .phsp file
* A .phsp file contains all the details of all the saved particles

We support three formats for Phase Space:

* ASCII provides particle information in an easy to read simple text file, which data encoded as a series of columns of text. The header file tells the contents and column order per particle.
* Binary provides the same information as ASCII, but in a much more compact format, with data encoded in a stream of bytes. The header file tells the contents and byte order per particle. Use Binary in cases where the ASCII format produces excessively large files.
* Limited is an alternate binary format compatible with some legacy codes. It has fewer options for what data can be expressed, but is compatible with codes such as that used by Varian for their TrueBeam phase space files. Use Limited format only when you need to exchange phase space with legacy codes.

You can additionally write phase space to ROOT files, however there is no corresponding ability to read phase space back in from these files.

You tell TOPAS what format to write out by setting::

    s:Sc/MyScorer/OutputType = "ASCII" # "Binary", "ASCII," "Limited" or "ROOT"

All formats provide at least ten quantities for each scored particle:

* X position
* Y position
* Z position
* U (direction cosine of momentum with respect to X)
* V (direction cosine of momentum with respect to Y)
* Energy in MeV
* Weight
* Particle ID
* Flag to tell if Third Direction Cosine is Negative (1 means true)
* Flag to tell if this is the First Scored Particle from this History (1 means true) (Note that this may or may not be the primary, as the primary may or may not have made it all the way to the scoring plane).

The positions are relative to the center of the World.

For the ASCII and Binary formats, you can turn on additional columns of phase space output::

    b:Sc/MyScorer/IncludeTOPASTime = "True" # Time used by TimeFeatures for this history
    b:Sc/MyScorer/IncludeTimeOfFlight = "True" # Time of Flight of this particle from start of history to scoring plane
    b:Sc/MyScorer/IncludeRunID = "True"
    b:Sc/MyScorer/IncludeEventID = "True"
    b:Sc/MyScorer/IncludeTrackID = "True"
    b:Sc/MyScorer/IncludeParentID = "True" # Track ID of parent particle
    b:Sc/MyScorer/IncludeCharge = "True"
    b:Sc/MyScorer/IncludeVertexInfo = "True" # Initial KE, Position and Momentum
    b:Sc/MyScorer/IncludeSeed = "True"

The last of these gives the four variable parts of a random seed. Replaying this random seed will get you the same event back later. The full random seed should be a file of the form:

.. code-block:: text

    Uvec
    1878463799
    3
    1425618182
    1466214412

To reuse a saved seed, create a file with the above five lines, replacing the four numeric parts with the four integers in the phase space file. Assuming you name that file "event1.rndm", you can then make TOPAS start from this random seed by having TOPAS wake up at the Geant4 command line, by using::

    Ts/PauseBeforeSequence = "True"

And then typing:

.. code-block:: text

    /random/resetEngineFrom event1.rndm
    exit

The phase space scorer and any custom n-tuple scorers buffer output to avoid excessive disk access. You will not generally need to adjust this buffering value, but can adjust if if you wish::

    i:Sc/MyScorer/OutputBufferSize = 1000 # Number of particles in phase space buffer

For more detail on Phase Space formats, see Miscellaneous Notes at the end of this User Guide.
