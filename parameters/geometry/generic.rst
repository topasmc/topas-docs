Generic Components
------------------

You can create a Geometry Component for any of the standard solids defined in the geometry section of the `Geant4 Application Developers Guide <http://geant4.web.cern.ch/geant4/UserDocumentation/UsersGuides/ForApplicationDeveloper/html/ch04.html#sect.Geom.Solids>`_.

The :ref:`example_basic_shapesall` example demonstrates how to build each of the solids.

.. image:: generic.png

Below we list the parameters for each Geant4 solid.
Further details about the parameters, along with helpful diagrams, can be found in the `Geant4 Application Developers Guide <http://geant4.web.cern.ch/geant4/UserDocumentation/UsersGuides/ForApplicationDeveloper/html/ch04.html#sect.Geom.Solids>`_.
All parameters are type ``d:`` unless otherwise noted below.
Some of these parameters have default values. If so, the default value is shown in parentheses. For most solids, sizes are specified in Half Lengths, denoted with an HL, such as HLX.
For a few solids, sizes are specified in full Lengths, denoted with just L, such as LX.


================  =========================================
G4Box             use :ref:`TsBox <geometry_dividable>` instead
G4Tubs            use :ref:`TsCylinder <geometry_dividable>` instead
G4CutTubs         RMin (0), RMax, HL, SPhi (0), DPhi (360 deg),
                  LowNorm, HighNorm (these are both ``uv:`` with length of 3)
G4Cons            RMin1 (0), RMax1, RMin2 (0), RMax2, HL, SPhi (0), DPhi (360 deg)
G4Para            HLX, HLY, HLZ, Alpha, Theta, Phi
G4Trd             HLX1, HLX2, HLY1, HLY2, HLZ
G4RTrap           LZ, LY, LX, LTX
G4GTrap           HLZ, Theta, Phi, HLY1, HLX1, HLX2, Alp1, HLY2, HLX3, HLX4, Alp2
G4Sphere          use :ref:`TsSphere <geometry_dividable>` instead
G4Orb             R
G4Torus           RMin (0), RMax, RTor, SPhi (0), DPhi (360 deg)
G4HPolycone       PhiStart, PhiTotal,
                  Z, RInner, ROuter (these three are ``dv:`` with length of numZPlanes)
G4SPolycone       PhiStart (0), PhiTotal (360 deg),
                  R, Z (these two are ``dv:`` with length of numZPlanes)
G4HPolyhedra      PhiStart (0), PhiTotal (360 deg), NSides (``i:``),
                  Z, RInner, ROuter (these three are ``dv:`` with length of numZPlanes)
G4SPolyhedra      PhiStart (0), PhiTotal (360 deg), NSides (``i:``),
                  R, Z (these two are ``dv:`` with length of numRZ)
G4EllipticalTube  HLX, HLY, HLZ
G4Ellipsoid       HLX, HLY, HLZ, ZBottom (-HLZ), ZTop (HLZ)
G4EllipticalCone  HLX, HLY, ZMax, ZTop (ZMax)
G4Paraboloid      HLZ, R1, R2
G4Hype            IR (0), OR, IS (0), OS, HLZ
G4Tet             Anchor, P2, P3, P4 (these four are ``dv:`` with length of 3)
G4Extruded        Polygons (``dv:`` with length of 2 x number of polygons),
                  HLZ, Off1 (``dv:`` with length of 2), Scale1 (``uv:``),
                  Off2 (``dv:`` with length of 2), Scale2 (``uv:``)
G4TwistedBox      Twist, HLX, HLY, HLZ
G4RTwistedTrap    Twist, HLX1, HLX2, HLY, HLZ
G4GTwistedTrap    Twist, HLZ, Theta, Phi, HLY1, HLX1, HLX2, HLY2, HLX3, HLX4, Alpha
G4TwistedTrd      HLX1, HLX2, HLY1, HLY2, HLZ, Twist
G4GenericTrap     HLZ, Vertices (``dv:`` with length of 2 x number of vertices
G4TwistedTubs     Twist, EndInnerRad, EndOuterRad, HLZ, Phi
================  =========================================

Some examples of components that can be built just from TsGenericComponents:

* Scatterer
* Collimator
* Mirror
* Water Tank
* Rando Phantom (as constructive solid geometry rather than DICOM import)
* Pin Diode Chamber
* Flat Panel Imaging Device
* Standard Ion Chamber
* Segmented Ion Chamber
* Faraday Cup

We have built some complex things just from combinations of the above Generic Components (such as the STAR radiosurgery beamline at MGH).
