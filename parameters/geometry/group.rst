Group Component
---------------

Creates no actual solid, but still has a placement (Trans and Rot).
Other components placed within this Group component are affected by this placement just as if the group were an enclosing box component.

The following defines a group component called "MyGroup"::

    s:Ge/MyGroup/Type="Group"
    s:Ge/MyGroup/Parent = "World"
    d:Ge/MyGroup/TransX=2. m
    d:Ge/MyGroup/TransY=2. m
    d:Ge/MyGroup/TransZ=0. m
    d:Ge/MyGroup/RotX=0. deg
    d:Ge/MyGroup/RotY=0. deg
    d:Ge/MyGroup/RotZ=30. deg

The following example shows how a Group Component, "Jaws", placed in a nozzle, allows one to position two individual movable collimator blocks, "Jaw_Upper" and "Jaw_Lower", without the creation of an extraneous mother volume::

    s:Ge/Jaws/Type = "Group"
    s:Ge/Jaws/Parent = "Nozzle"
    d:Ge/Jaws/TransZ = 0. m
    ...
    s:Ge/Jaw_Upper/Type = "TsBox"
    s:Ge/Jaw_Upper/Parent = "Jaws"
    s:Ge/Jaw_Upper/Material = "Tungsten"
    d:Ge/Aperture/TransY = 2. cm
    ...
    s:Ge/Jaw_Lower/Type = "TsBox"
    s:Ge/Jaw_Lower/Parent = "Jaws"
    s:Ge/Jaw_Lower/Material = "Tungsten"
    d:Ge/Aperture/TransY = -2. cm
    ...
