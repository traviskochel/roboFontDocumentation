.. _sliceTool:

Slice Tool
==========

.. image:: /static/cursorSlice.png

Will add points on dragged slice line.

.. image:: /static/sliceLine.png

.. cssclass:: doctable

+------------+------------------------------------------+
| click      | add a starting point of a slice line     |
+------------+------------------------------------------+
| drag       | sets end point of slice line             |
+------------+------------------------------------------+
| drag shift | adjust slice line on x, y or 45°         |
+------------+------------------------------------------+
| mouse up   | slice the glyph according the slice line |
+------------+------------------------------------------+

When the slice line has 2 intersection on the same contour it will cut the contour, otherwise is will just add points.
(Guides can also slice see :ref:`guides`)