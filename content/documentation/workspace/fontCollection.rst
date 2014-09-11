.. _fontCollection:

Font Collection
===============

.. image:: /static/fontCollection.png

The Font Collection displays an overview of all the glyphs contained the font. It has several tools and functions to create and manage glyph collections, and to order the glyphs in the window.

.. toctree::
    :maxdepth: 2
    :titlesonly:

    fontCollection/addingAndDeletingGlyphs
    fontCollection/markGlyphs
    fontCollection/sort
    fontCollection/smartSets
    fontCollection/searchAndFind
    fontCollection/displayModes

Users can define a preset character set to display 'glyphs-still-to-draw'.

Read more: :ref:`preferences`

.. cssclass:: doctable

+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| single click                           | Select single glyph                                                                                                               |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| single click + alt (multi window mode) | Opens a new glyph window.                                                                                                         |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| single click (single window mode)      | Select single glyph and send it to the glyph view                                                                                 |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| double click (single window mode)      | Send the glyph to the glyph view                                                                                                  |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| click + drag                           | **Drag the selection on the same Font Overview**                                                                                  |
|                                        | * Drop between the glyph cells: reorder the glyph order of the font.                                                              |
|                                        | * Drop on a glyph cell: copy the dragged glyphs in the destination glyph cell,                                                    |
|                                        | use alt down to copy as component.                                                                                                |
|                                        | **Drag the selection to other views**                                                                                             |
|                                        | * Other Font Collection View: add the glyphs to the other font and set the order of dropped between glyph cells.                  |
|                                        | * Space Center: set the glyph names to as input for spacing, use alt to append the glyph names.                                   |
|                                        | * Smart sets: creates a new set with the dragged glyphs.                                                                          |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| click + command + drag                 | Alter the selection while moving the mouse.                                                                                       |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| copy                                   | Copies the selected glyphs to the clip board as glyph objects and the glyph names as string representation.                       |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| copy as component                      | Copies the selected glyph as component, only if a single glyph is selected.                                                       |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| paste                                  | * If there is no selection it appends the copied glyphs to the font.                                                              |
|                                        | * If amount of the selected glyphs is the same as the amount of copied glyphs, RoboFont will replace them with the copied glyphs. |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| undo/redo                              | Undo or redo the selected glyph(s)                                                                                                |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| start typing a glyph name              | Tries to find and select that glyph                                                                                               |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| ⌘ + J                                  | Opens a Jump To Glyph window.                                                                                                     |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| delete                                 | Remove the glyph from the font                                                                                                    |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| alt + delete                           | Remove the glyph from the font and the template glyph from the Font Overview.                                                     |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+

