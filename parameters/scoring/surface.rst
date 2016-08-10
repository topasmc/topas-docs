.. _scoring_surface:

Surface Scorers
---------------

Surface Scorer Quantities are:

* SurfaceCurrent
* SurfaceTrackCount
* PhaseSpace

Surface Scorers must indicated the relevant ``Component`` and ``Surface`` name::

    s:Sc/MyScorer/Surface = "Phantom/ZMinusSurface"

where the surface name refers to the coordinate system of the ``Component``.

The syntax to specify surface depends on which shape component is involved.

* For TsBox:

    * XMinusSurface
    * XPlusSurface
    * YMinusSurface
    * YPlusSurface
    * ZMinusSurface
    * ZPlusSurface

* For TsCylinder:

    * ZMinusSurface
    * ZPlusSurface
    * InnerCurvedSurface
    * OuterCurvedSurface
    * PhiMinusSurface (if cut or divided along Phi)
    * PhiPlusSurface (if cut or divided along Phi)

* For TsSphere:

    * InnerCurvedSurface
    * OuterCurvedSurface
    * PhiMinusSurface (if cut or divided along Phi)
    * PhiPlusSurface (if cut or divided along Phi)
    * ThetaMinusSurface (if cut or divided along Theta)
    * ThetaMinusSurface (if cut or divided along Theta)

If you are scoring on a :ref:`divided component <geometry_dividable>` (TsBox, TsCylinder or TsSphere), all surfaces of the divided component then become sensitive for scoring. So, for example, ZMinusSurface will mean to accumulate hits on every ZMinusSurface of every voxel in the divided TsBox.

Creators of parameter files can pre-define more user-friendly synonyms through relative parameters, such as::

    s:Ge/WaterTank/Water/UpstreamSurface = Ge/WaterTank/Water/ZMinusSurface

so that users can then score using the named ``Surface``, as in::

    s:Sc/MyScorer/Surface = Ge/WaterTank/Water/UpstreamSurface
