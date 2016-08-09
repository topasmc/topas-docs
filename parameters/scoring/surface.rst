Surface scorers
---------------

Surface Scorer Quantities are:

* SurfaceCurrent
* SurfaceTrackCount
* PhaseSpace

Surface Scorers must indicated the relevant Component and Surface name::

    s:Sc/MyScorer/Surface = "Phantom/ZMinusSurface"

where the X, Y or Z refers to the coordinate system of the Component.

The syntax to specify surface depends on which shape component is involved.

* For TsBox:
    * XMinusSurface # in coordinate system of the Component
    * XPlusSurface
    * YMinusSurface
    * YPlusSurface
    * ZMinusSurface
    * ZPlusSurface
* For TsCylinder:
    * ZMinusSurface # in coordinate system of the Component
    * ZPlusSurface
    * InnerCurvedSurface
    * OuterCurvedSurface
    * PhiMinusSurface - relevant if cylinder or tubs has been cut or divided along Phi
    * PhiPlusSurface - relevant if cylinder or tubs has been cut or divided along Phi
* For TsSphere:
    * InnerCurvedSurface
    * OuterCurvedSurface
    * PhiMinusSurface - relevant if cylinder or tubs has been cut or divided along Phi
    * PhiPlusSurface - relevant if cylinder or tubs has been cut or divided along Phi
    * ThetaMinusSurface - relevant if cylinder or tubs has been cut or divided along Theta
    * ThetaMinusSurface - relevant if cylinder or tubs has been cut or divided along Theta

If you are scoring on a divided component (TsBox, TsCylinder or TsSphere), all surfaces of the divided component then become sensitive for scoring. So, for example, ZMinusSurface will mean to accumulate hits on every ZMinusSurface of every voxel in the divided TsBox.

Creators of parameter files can pre-define more user-friendly synonyms through relative parameters, such as::

    s:Ge/WaterTank/Water/UpstreamSurface = Ge/WaterTank/Water/ZMinusSurface

so that users can then score using these named Surfaces, as in::

    s:Sc/MyScorer/Surface = WaterTank/Water/UpstreamSurface
