Visualization Attributes
------------------------

By default, Components are colored according to their materials, based on the default color that was assigned to the material, such as::

    s:Ma/Air/DefaultColor="lightblue"

Parameters of the Component let you override this color and set other visualization attributes::

    s:Ge/MyComponent/Color = "red"
    s:Ge/MyComponent/DrawingStyle = "Solid" # "Solid", "Wireframe" or "FullWireFrame"
    i:Ge/MyComponent/VisSegsPerCircle = 100 # Number of line segments to use to approximate a circle, defaults to 24
    b:Ge/MyComponent/Invisible = "True" # defaults to False meaning visible

FullWireFrame includes drawing of additional edge lines that Geant4 calls "soft edges" - on many graphics devices WireFrame and FullWireFrame give the same result.

Increase VisSegsPerCircle if you want a smoother curve.
