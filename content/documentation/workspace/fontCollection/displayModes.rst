..  _displayModes:

Display Modes
=============

The Font Collection View has two display modes, 'Tiled glyphs' aka "glyph cells" and 'Glyph list'. Users can switch between those two display options by clicking on the icons at the lower left of the Font Collection window.

.. image:: /static/displayModes.png

Tiled glyph mode
----------------

.. image:: /static/fontCollectionLargeCells.png

Depending on the size of the tile it will display more information about the glyph (name, metrics, layers).

The size can be adjusted by zooming in or out or by adjusting the slider in at the bottom.

Unsaved glyphs have their names highlighted until the font saved again.

Marked glyphs will display the mark color in the glyph cell.

A colored L at the bottom right indicates that the glyph contains more than one layer.

A gray N at the bottom right indicates that the glyph as a note.

Glyph list mode
---------------

.. image:: /static/fontCollectionListMode.png

The glyph list mode displays all glyphs as a big table, showing different kinds of glyph data.

This view makes it possible for users to perform search operations for different kinds of glyph data.

Right-clicking in the table header activates a contextual menu which lets users turn individual data columns on/off.

.. cssclass:: doctable

+-----------------------------------+-----------------------------------------------------------+
| preview                           | glyph thumbnail                                           |
+-----------------------------------+-----------------------------------------------------------+
| name                              | glyph name                                                |
+-----------------------------------+-----------------------------------------------------------+
| left sidebearing                  | glyph left sidebearing                                    |
+-----------------------------------+-----------------------------------------------------------+
| right sidebearing                 | glyph right sidebearing                                   |
+-----------------------------------+-----------------------------------------------------------+
| width                             | glyph width                                               |
+-----------------------------------+-----------------------------------------------------------+
| unicode                           | glyph unicode                                             |
+-----------------------------------+-----------------------------------------------------------+
| contours                          | amount of contours in the glyph                           |
+-----------------------------------+-----------------------------------------------------------+
| components                        | amount of components in the glyph                         |
+-----------------------------------+-----------------------------------------------------------+
| amount of components in the glyph | a comma seperated list of all components base glyph names |
+-----------------------------------+-----------------------------------------------------------+
| anchors                           | amount of anchors                                         |
+-----------------------------------+-----------------------------------------------------------+
| anchor names                      | a comma seperated list of all anchor names                |
+-----------------------------------+-----------------------------------------------------------+
| color                             | the mark color of the glyph                               |
+-----------------------------------+-----------------------------------------------------------+
| empty                             | a bool indicating if the glyph is empty                   |
+-----------------------------------+-----------------------------------------------------------+
| template                          | a bool indicating if the glyph is a template glyph        |
+-----------------------------------+-----------------------------------------------------------+
| glyph changed                     | a bool indicating if the glyph has changed                |
+-----------------------------------+-----------------------------------------------------------+

The displayed glyph data can be used to search and find glyphs or make smart sets.

Read more: :ref:`searchAndFind`, :ref:`smartSets`

