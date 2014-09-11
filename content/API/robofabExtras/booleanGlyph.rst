.. _booleanGlyph:

Boolean Glyph
=============

RoboFont makes it possible to perform common boolean path operations (difference, union, intersection and exclusive or) with glyph objects directly, using special characters as operators.

.. cssclass:: doctable

+---------------+----------+
| operation     | operator |
+===============+==========+
| difference    | %        |
+---------------+----------+
| union         |  \|      |
+---------------+----------+
| interesection | &        |
+---------------+----------+
| exclusive or  | ^        |
+---------------+----------+

Example
-------

.. image:: /static/booleanOperations.png

Here are the four boolean path operations in action. Note that, for the difference operation, the order of the operands matters.

.. showcode:: /RoboFontExamples/glyphs/booleanGlyphMath.py

Read more: `booleanOperations <https://github.com/typemytype/booleanOperations>`_