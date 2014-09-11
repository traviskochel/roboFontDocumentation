.. _mojo.tools:

mojo.tools
==========

::

    from mojo.tools import *

.. function:: IntersectGlyphWithLine(glyph, ((sx, sy), (ex, ey)), canHaveComponent=False, addSideBearings=False)

    Returns a list of intersections of a glyph with a given line.

.. function:: union(glyph, subjectContours, clipContours, roundCoordinates=None)

    perform a union with subject contours and clip contours
    glyph: destination glyph
    subjectContours, clipContours: for union its not really important so you can mix both
    roundCoordinates: optionally round the result

.. function:: intersect(glyph, subjectContours, clipContours, roundCoordinates=None)

    perform a intersection with subject contours and clip contours
    glyph: destination glyph
    subjectContours: the subject contours
    clipContours: the clip contours that will intersect with the subject contours
    roundCoordinates: optionally round the result

.. function:: difference(glyph, subjectContours, clipContours, roundCoordinates=None)

    perform a difference with subject contours and clip contours
    glyph: destination glyph
    subjectContours: the subject contours
    clipContours: the clip contours that will difference with the subject contours
    roundCoordinates: optionally round the result

.. function:: intersection(glyph, subjectContours, clipContours, roundCoordinates=None)

    perform a intersection with subject contours and clip contours
    glyph: destination glyph
    subjectContours: the subject contours
    clipContours: the clip contours that will intersection with the subject contours
    roundCoordinates: optionally round the result

.. function:: xor(glyph, subjectContours, clipContours, roundCoordinates=None)

    perform a xor with subject contours and clip contours
    glyph: destination glyph
    subjectContours: the subject contours
    clipContours: the clip contours that will xor with the subject contours
    roundCoordinates: optionally round the result


.. class:: BooleanGlyph(glyph, roundCoordinates=None)

    A object that can be used to perform simple math operations and acts like a glyph object.

    Read more: :ref:`booleanGlyph`

    .. describe:: glyph

        the source glyph

    .. describe:: roundCoordinates

        optionally round the result

    .. function:: draw(pen)

        draws the booleanGlyph in a pen

    .. function:: drawPoints(pointPen)

        draws the booleanGlyph in a pointPen

    .. function:: union(other)

        performs an union operation

        ::

            BooleanGlyph(glyph) | BooleanGlyph(glyph2)

    .. function:: difference(other)

        performs a difference operation

        ::

            BooleanGlyph(glyph) - BooleanGlyph(glyph2)


    .. function:: intersection(other)

        performs a intersection operation

        ::

            BooleanGlyph(glyph) & BooleanGlyph(glyph2)

    .. function:: xor(other)

        performs a xor operation

        ::

            BooleanGlyph(glyph) ^ BooleanGlyph(glyph2)

    .. attribute:: width

        returns the width of the booleanGlyph