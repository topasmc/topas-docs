.. _geometry_dividable:

Dividable Components
--------------------

==========  =============   =======   ==============
Type        Parameters      Type      Default value
==========  =============   =======   ==============
TsBox       | XBins         | i       | 1
            | YBins         | i       | 1
            | ZBins         | i       | 1
TsCylinder  | RBins         | i       | 1
            | PhiBins       | i       | 1
            | ZBins         | i       | 1
TsSphere    | RBins         | i       | 1
            | PhiBins       | i       | 1
            | ThetaBins     | i       | 1
==========  =============   =======   ==============


.. image:: dividable.png

Scorers associated with the dividable components may use the same or different divisions (thus one can do things like represent the patient with CT resolution but score with other resolutions). See :ref:`here <scoring_binning_space>` for details.

You cannot place child components inside a divided component, but if the only reason for dividing this component is to have fine-grained scoring, you can easily work around this limitation. Use an undivided parent component. Place the children into this undivided parent component. Then when you specify that you want to score on this parent component, specify divided scoring (see :ref:`here <scoring_binning_space>`). TOPAS will automatically create a parallel world version of your component to handle the divided scoring.

You can optionally specify different materials for each voxel, overriding the value set in the regular ``Ge/.../Material`` parameter::

    sv:Ge/Phantom/VoxelMaterials = 100 "G4_WATER" "G4_WATER" "Air" "Air" "G4_WATER" ...

This means you can create complex phantoms directly from the parameter system.
``VoxelMaterials`` works for all three kinds of divided components: TsBox, TsCylinder and TsSphere. See the :ref:`example_scoring_voxelmaterials` example.
