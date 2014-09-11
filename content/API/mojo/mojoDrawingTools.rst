.. _mojo.drawingTools:

mojo.drawingTools
=================

::

    from mojo.drawingTools import *


Using similar tools to draw in Cocoa object like `DrawBot <http://drawbot.com>`_.

.. function:: save()

    save the current graphic state

.. function:: restore()

    restore the current graphic state

.. function:: rect(x, y, width, height)

    draws a rectangle

.. function:: oval(x, y, width, height)

    draws an oval

.. function:: newPath()

    creates a new path

.. function:: moveTo((x, y))

    move to point

.. function:: lineTo((x, y))

    line to point

.. function:: curveTo((h1x, h1y), (h2x, h2y), (x, y))

    curve to point with bcps

.. function:: closePath()

    close the path

.. function:: drawPath()

    draws the path

.. function:: fill(r, g, b, a=1)

    Set the fill color as RGB value.

.. function:: stroke(r, g, b, a=1)

    Set the stroke color as RGB value.

.. function:: strokeWidth(value)

    Set the stroke width for a path.

.. function:: miterLimit(value)

    Set the miter limit for a path.

.. function:: lineJoin(join)

    Set the line join for a path, possible join arguments are: *bevel*, *miter* or *round*

.. function:: dashLine(dash)

    dash is a list of of values

.. function:: translate(x, y)

    Translate the art board pane to *x*, *y*

.. function:: rotate(angle)

    Rotate the art board by an angle.

.. function:: scale(x, y)

    Scale the art board by *x*, *y*, if *y* is not set the art board will be scaled proportionally.

.. function:: skew(a, b)

    Skew the art board by *a*, *b*, if *b* is not set the art board will be skew with *a* = *b*

.. function:: font(fontName, fontSize=None)

    Set the font by PostScript name.
    Optionally set the font size.

.. function:: fontSize(fontSize)

    Set the font size.

.. function:: text(textString, (x, y))

    Draw a text on position *x*, *y*.

.. function:: image(filePath, (x, y), alpha=1)

    Draw an image on position *x*, *y*.
    Optionally set an alpha value.