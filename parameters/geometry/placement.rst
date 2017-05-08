.. _geometry_placement:

Placement of Components
-----------------------

A component's ``Parent`` parameter tells which other component the current one is a child of. In this way, one can build a hierarchy of components::

    s:Ge/MyComponent/Parent = SomeOtherComponent

The one component that is always provided automatically for you, into which you plug the rest of your hierarchy, is called ``World``.

Each component has three translation and three rotation parameters.
These give the position of the component in the coordinate system of its parent component.

The following defines a box of air with half width of 5 m on each side placed at the center of the world::

    s:Ge/MyBox/Type="TsBox"
    s:Ge/MyBox/Parent = "World"
    s:Ge/MyBox/Material="Air"
    d:Ge/MyBox/HLX=5. m # Half Length
    d:Ge/MyBox/HLY=5. m
    d:Ge/MyBox/HLZ=5. m
    d:Ge/MyBox/TransX=0. m
    d:Ge/MyBox/TransY=0. m
    d:Ge/MyBox/TransZ=0. m
    d:Ge/MyBox/RotX=0. deg
    d:Ge/MyBox/RotY=0. deg
    d:Ge/MyBox/RotZ=0. deg

If you set more than one rotation, note that rotation happens first around X, then the Y rotation is applied around the now-rotated axes, and then the Z rotation is applied around those rotated axes. In general, a way to keep rotations more clear is to use intermediate Group components as follows:

* Place your component inside a Group component.
* Rotate your component around one axis.
* Rotate the group component around the other axis.

While the direction of rotation can be confusing, the correctness of rotations in TOPAS has been double, triple and quadruple checked and found consistent with the definitions in Geant4.
The :ref:`example_timefeature_rotation` example shows an object being rotated first in the positive X direction, then in the positive Y direction, then in the positive Z direction.

For Geant4 experts, be advised that the rotation angles you provide to TOPAS are passed into ``G4RotationMatrix()->rotateX/Y/Z``. Further discussion of Geant4 rotations can be found `here <http://hypernews.slac.stanford.edu/HyperNews/geant4/get/geometry/1408>`_.

The following overrides the size definition of the ``World`` box that was inherited from the :ref:`built-in default parameters <parameters_default_world>` and then inserts a box into this world and another box into the first box::

    # Overrides the world size that was set in built-in defaults:
    Ge/World/HLX=10. m
    Ge/World/HLY=10. m
    Ge/World/HLZ=10. m

    # Box inserted into the World
    s:Ge/TestBox/Material="Air"
    s:Ge/TestBox/Parent="World"
    s:Ge/TestBox/Type="TsBox"
    d:Ge/TestBox/HLX=400. cm
    d:Ge/TestBox/HLY=300. cm
    d:Ge/TestBox/HLZ=200. cm
    d:Ge/TestBox/TransX=0. m
    d:Ge/TestBox/TransY=0. cm
    d:Ge/TestBox/TransZ=0. m
    d:Ge/TestBox/RotX=0. deg
    d:Ge/TestBox/RotY=0. deg
    d:Ge/TestBox/RotZ=0. deg

    # Another box inserted into the first box
    s:Ge/TestBox2/Material="Carbon"
    s:Ge/TestBox2/Parent="TestBox"
    s:Ge/TestBox2/Type="TsBox"
    d:Ge/TestBox2/HLX=180. cm
    d:Ge/TestBox2/HLY=120. cm
    d:Ge/TestBox2/HLZ=80. cm
    d:Ge/TestBox2/TransX=0. m
    d:Ge/TestBox2/TransY=0. cm
    d:Ge/TestBox2/TransZ=150. cm
    d:Ge/TestBox2/RotX=0. deg
    d:Ge/TestBox2/RotY=30. deg
    d:Ge/TestBox2/RotZ=0. deg



Overlap Checking
~~~~~~~~~~~~~~~~

Because accidental overlaps of geometry volumes are a serious issue for all Monte Carlo simulations, Geant4 provides tools to automatically check for such overlaps. Overlap checking is not perfect, it works by testing a random set of points on each boundary, to see if they are inside any other boundary. Thus it will not necessarily find all overlaps. By default TOPAS checks 100 points on each volume. Overlap checking has a speed cost at initialization time, so once you are confident that your geometry has no overlaps, you may choose to turn this feature off (though most users never find this necessary)::

    Ge/CheckForOverlaps = "False"

TOPAS will save time by avoiding overlap checking for individual parts within a divided component (such as the voxels within a patient) since these subdivisions are generated automatically by our own code. But if you ever want to turn these back on::

    b:Ge/CheckInsideEnvelopesForOverlaps = "True"

You can control the number of points used in the overlap check::

    i:Ge/CheckForOverlapsResolution = 1000

And you can check the tolerance for overlap::

    d:Ge/CheckForOverlapsTolerance = 0. mm

You can also set these in a more granular fashion, per Component (overrides the above parameters for this particular component)::

    i:Ge/MyComponent/CheckForOverlapsResolution = 1000
    d:Ge/MyComponent/CheckForOverlapsTolerance = 0. mm



Pre-Defining Values
~~~~~~~~~~~~~~~~~~~

It may be useful to pre-define a range of named-values, such that you can easily access the values later. For example, we pre-define the angles at which certain scatterers are stored on a scatterer selection wheel::

    d:Ge/Gantry1/Scatterer2/RotZForSS0 = 0. deg
    d:Ge/Gantry1/Scatterer2/RotZForSS8 = 270. deg
    d:Ge/Gantry1/Scatterer2/RotZForSS2 = 180. deg
    d:Ge/Gantry1/Scatterer2/RotZForSS3 = 90. deg

And then in our user file, the user doesn't have to know these actual angles, but can just rotate to one of the named scatterers::

    Ge/Scatterer2/Holder/RotZ = Ge/Gantry1/Scatterer2/RotZForSS3 deg
