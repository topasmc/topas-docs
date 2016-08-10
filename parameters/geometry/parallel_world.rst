.. _geometry_parallel:

Parallel Worlds
---------------

Components can be assigned to "parallel worlds" rather than the standard, mass world.
Such components have no effect on physics (other than usually very minor step limitation effects) but can still be used for scoring. Such components can arbitrarily overlay the mass world. Their volumes can overlap any other volumes in other mass or parallel worlds.
To assign a component to a parallel world, include the line::

    b:Ge/MyComponent/IsParallel = "True"

* Parallel world components may be children of other parallel world components.
* Parallel world components may be children of mass world components.
* Mass world components may not be children of parallel world components.

A new parallel world will be created each time you specify ``IsParallel``, with an automatically generated parallel world name based on the component name. If you want to explicitly assign multiple components to the same parallel world, provide the additional parameter::

    s:Ge/MyComponent/ParallelWorldName = "SomeParallelWorldName"

This is useful if you will have many components in parallel worlds, as Geant4 only allows up to 8 total worlds.

.. warning::

    In certain cases, TOPAS must represent a geometry by using a Geant4 technique called "parameterized volumes." However we have found that Geant4 behaves unreliably if parameterized sphere is placed in a parallel world. Accordingly, TOPAS applies a safety restriction:

    * TsSphere can not be in a parallel world if it has any divisions.



Layered Mass Geometry
~~~~~~~~~~~~~~~~~~~~~

Components that are in a parallel world can have material or not. If they have material, and they are listed in the ``LayeredMassGeometryWorlds`` parameter, this material will take precedence over any real world material found in that location.

In Geant4 this is called Layered Mass Geometry. It is further described in (`PubMed <http://www.ncbi.nlm.nih.gov/pubmed/22975747>`_):

Enger S et al, "Layered mass geometry: a novel technique to overlay seeds and applicators onto patient geometry in Geant4 brachytherapy simulations," Phys Med Biol. 2012 Oct 7;57(19):6269-77.

Any time a component in a parallel world has material, that world must be listed in the ``LayeredMassGeometryWorlds`` parameter. The parameter is a string vector because any number of parallel worlds can have material. The order of the worlds in this parameter is significant. Material from worlds listed later in this list take precedence over material in worlds listed earlier. Thus, in the following example, material in the world ``Seed`` will take precedence over material in the world ``Tumor`` which will take precedence over material in the regular world::

    sv:Ph/Default/LayeredMassGeometryWorlds = 2 "Tumor" "Seed"

A simple example is provided in :ref:`example_basic_layeredmassgeometry`.
