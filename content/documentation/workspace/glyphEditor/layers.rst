.. _layers:

Layers
======

RoboFont can handle layers inside a single UFO. The idea is to have it very flexible. Some will use it as a way to separate different stages of a font. Others will use it as way to collaborate and other others will use it like multiple master.

Users can add, delete, reorder layers in the layer inspector pane.

.. image:: /static/inspectorLayersPane.png

There is no limit on the amount of layers in a glyph.

Layers names are ASCII without spaces, slashes and semicolons.

Layers can have any color. Used to be displayed in the background of the glyph editor.

.. cssclass:: doctable

+-------------------+-------------------------------------------------------------------------------------------------------+
| \+                | add layer                                                                                             |
+-------------------+-------------------------------------------------------------------------------------------------------+
| \-                | remove layer                                                                                          |
+-------------------+-------------------------------------------------------------------------------------------------------+
| eye               | toggle the selected layer visibility when displayed in the background of the glyph editor             |
+-------------------+-------------------------------------------------------------------------------------------------------+
| filled rectangle  | toggle the selected layer fill when displayed in the background of the glyph editor                   |
+-------------------+-------------------------------------------------------------------------------------------------------+
| stroked rectangle | toggle the selected layer stroke when displayed in the background of the glyph editor                 |
+-------------------+-------------------------------------------------------------------------------------------------------+
| point             | toggle the selected layer show points when displayed in the background of the glyph editor            |
+-------------------+-------------------------------------------------------------------------------------------------------+
| coordinate        | toggle the selected layer show point coordinates when displayed in the background of the glyph editor |
+-------------------+-------------------------------------------------------------------------------------------------------+

Read more: :ref:`inspector`