.. _mojo.glyphPreview:

mojo.glyphPreview
=================

::

    from mojo.glyphPreview import GlyphPreview


.. class:: GlyphPreview(posSize, contourColor=None, componentColor=None, selectionColor=None)

    A vanilla group subclass that previews a glyph.

    .. describe:: posSize

        Tuple of 4 (left, top, right, bottom), those numbers can be negative.

    .. describe:: contourColor

        A NSColor object used to draw the contours, optionally.

    .. describe:: componentColor

        A NSColor object used to draw the components, optionally.

    .. describe:: selectionColor

        A NSColor object used to draw the selection.

    .. function:: setGlyph(glyph)

        Set a glyph in the preview.

    .. function:: setSelection(points)

        Sets a list of points to display.


.. showcode:: /RoboFontExamples/UI/glyphPreviewExample.py