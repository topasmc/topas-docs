.. _source_volumetric:

volumetric Sources
------------------

volumetric sources emit particles from randomly sampled starting positions from within the radioactive volume of a given component.

This source type has been designed for Brachytherapy applications (though there may be other applications as well).

Specify source type as::

    s:So/MySource/Type = "Volumetric"

And then add an additional required parameter:

    s:So/*/ActiveMaterial

to specify which material within the given component should be considered radioactive.

So, for example, if you have:

    s:So/Example/Type                = "Volumetric"
    s:So/Example/Component       = "ActiveSource"
    sc:So/Example/ActiveMaterial = "G4_Ir"

particles will start from randomly sampled positions within the Iridium parts of the component named ActiveSource.

Examples that use this source can be found in:

* examples/Brachytherapy
* examples/Basic/VolumetricSource.txt

The energies and species of the emitted particles can be specified using the same parameters available to the :ref:`source_beam`.
