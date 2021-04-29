.. _scoring_phasespace:

Phase Space Scorer
------------------

Phase Space refers to the technique of saving or replaying a set of particles crossing a given surface. It is the only one of our built-in scorers that saves data to n-tuple format, rather than storing accumulated overall data (counts or averages). However you can write extension scorers to use this generalized n-tuple capability to store other information on a per-particle basis (see :ref:`extension_scoring`).

* When one saves a phase space, one defines a surface and then saves the position, particle type, energy and momentum of some or all particles crossing that surface.
* When one replays a phase space, one starts a set of particles from the saved positions, with the saved particle types, energy and momentum.

Phase Space enables separating two parts of a simulation or analysis job, and can be used to transfer sets of particles among different codes.

If your :ref:`Surface Scorer <scoring_surface>` has ``Quantity = "PhaseSpace"``, the output will be a pair of Phase Space files:

* A .header file tells the number of histories, the number of saved particles and the order of information in the .phsp file
* A .phsp file contains all the details of all the saved particles

Note that if your scoring Component is a divided component, such as a voxelized patient, phase space will be scored on the specified surface of Every Voxel (this is the same scoring behavior you will see from any other Surface Scorer in TOPAS).

We support three formats for Phase Space:

* ASCII provides particle information in an easy to read simple text file, which data encoded as a series of columns of text. The header file tells the contents and column order per particle.
* Binary provides the same information as ASCII, but in a much more compact format, with data encoded in a stream of bytes. The header file tells the contents and byte order per particle. Use Binary in cases where the ASCII format produces excessively large files.
* Limited is an alternate binary format compatible with some legacy codes. It has fewer options for what data can be expressed, but is compatible with codes such as that used by Varian for their TrueBeam phase space files. Use Limited format only when you need to exchange phase space with legacy codes.

You can additionally write phase space to `ROOT files <https://root.cern.ch>`_, however there is no corresponding ability to read phase space back in from these files.

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

The positions are relative to the center of the ``World``.

For the ASCII and Binary formats, you can turn on additional columns of phase space output::

    b:Sc/MyScorer/IncludeTOPASTime = "True" # Time used by TimeFeatures for this history
    b:Sc/MyScorer/IncludeTimeOfFlight = "True" # Time of Flight of this particle from start of history to scoring plane
    b:Sc/MyScorer/IncludeRunID = "True"
    b:Sc/MyScorer/IncludeEventID = "True"
    b:Sc/MyScorer/IncludeTrackID = "True"
    b:Sc/MyScorer/IncludeParentID = "True" # Track ID of parent particle
    b:Sc/MyScorer/IncludeCharge = "True"
    b:Sc/MyScorer/IncludeCreatorProcess = "True"
    b:Sc/MyScorer/IncludeVertexInfo = "True" # Initial KE, Position and Momentum
    b:Sc/MyScorer/IncludeSeed = "True"

The last of these gives the four variable parts of a random seed. Replaying this random seed will get you the same event back later. The full random seed should be a file of the form:

.. code-block:: plain

    Uvec
    1878463799
    3
    1425618182
    1466214412

To reuse a saved seed, create a file with the above five lines, replacing the four numeric parts with the four integers in the phase space file. Assuming you name that file ``event1.rndm``, you can then make TOPAS start from this random seed by having TOPAS wake up at the Geant4 command line, by using::

    Ts/PauseBeforeSequence = "True"

And then typing:

.. code-block:: plain

    /random/resetEngineFrom event1.rndm
    exit

The phase space scorer and any custom n-tuple scorers buffer output to avoid excessive disk access. You will not generally need to adjust this buffering value, but can adjust if if you wish::

    i:Sc/MyScorer/OutputBufferSize = 1000 # Number of particles in phase space buffer



.. _phasespace_format:

Phase Space Format
~~~~~~~~~~~~~~~~~~

Phase Space refers to the technique of saving or replaying a set of particles crossing a given surface.

* When one saves a phase space, one defines a surface and then saves the position, particle type, energy and momentum of some or all particles crossing that surface.
* When one replays a phase space, one starts a set of particles from the saved positions, with the saved particle types, energy and momentum.

Phase Space enables separating two parts of a simulation or analysis job, and can be used to transfer sets of particles among different codes.

A Phase Space is stored as a pair of related files:

* A .header file tells the number of histories, the number of saved particles and the order of information in the .phsp file
* A .phsp file contains all the details of all the saved particles

We support three formats for Phase Space:

* Binary is a compact format, with data encoded in a stream of bytes. The header file tells the contents and byte order per particle.
* ASCII provides the same information as Binary, but presents it as a much less compact, but easier to read simple text file, which data encoded as a series of columns of text. The header file tells the contents and column order per particle.
* Limited is an alternate binary format compatible with some legacy codes. It has fewer options for what data can be expressed, but is compatible with codes such as that used by Varian for their TrueBeam phase space files.

You can additionally write phase space to `ROOT files <https://root.cern.ch>`_, however there is no corresponding ability to read phase space back in from these files.

For the Binary and ASCII formats, Particle ID is encoded using the large set of integer codes specified by the Particle Data Group (PDG):

* 22 = photon
* 11 = electron
* -11 = positron
* 2112 = neutron
* 2212 = proton
* Additional codes go all the way up to ten digit ion codes of the form ±10LZZZAAAI.
* See the `PDG web site <http://pdg.lbl.gov/2012/mcdata/mc_particle_id_contents.html>`_ for a full explanation

For the Limited format, only a few particle codes are supported, while other particle types are not scored at all (and so this format is only recommended if you need to interface with legacy codes):

* 1 = photon
* 2 = electron
* 3 = positron
* 4 = neutron
* 5 = proton

The Binary and ASCII formats are self-describing, with the complete column or byte order documented in the associated header file. The exact set of columns will depend on which options are used to create the phase space file. Run the :ref:`example_phsp_ascii_write` and :ref:`example_phsp_binary_write` examples to see these headers.

If you are attempting to create TOPAS Binary or ASCII phase space from some application other than TOPAS, be advised that the formatting requirements are very specific. It is best to compare your phase space header and phsp files to those produced by the TOPAS examples listed above.
Some things to watch out for:

* First line of header has to be exactly as produced by TOPAS, with no extra spaces, tabs, etc.
* Integer values in the ASCII phase space must not contain decimal points

The Limited format uses the following byte order (the format is not self-describing):

=============   ========================================================
Size            Quantity
=============   ========================================================
1 byte          | Particle ID
                | Absolute value gives the particle code
                | Sign of this value encodes the direction of the 3rd direction cosine
4 bytes         | Energy
                | Absolute value gives the energy in MeV
                | Sign of this value is set to negative if this is the first scored particle from this history
4 bytes         X position
4 bytes         Y position
4 bytes         Z position
4 bytes         U (direction cosine of momentum with respect to X)
4 bytes         V (direction cosine of momentum with respect to Y)
4 bytes         Weight
=============   ========================================================

Direction cosines are consistent between Binary, ASCII and Limited formats. Descriptions can be found `on Wikipedia <https://en.wikipedia.org/wiki/Direction_cosine>`_ and `on MathWorld <http://mathworld.wolfram.com/DirectionCosine.html>`_. Direction cosines U, V and W correspond to direction cosines alpha, beta and gamma on those sites.
