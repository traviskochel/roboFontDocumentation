.. _searchAndFind:

Search And Find
===============

The Font Collection can search and find glyphs and save the search query.

Users can toggle the Search and Find bar in the toolbar of the Font Collection window in multi-window mode, or at the bottom of the window in single window mode, or use ⌘ + F.

.. image:: /static/searchAndFind.png

By clicking the '+'' in the top right of the font collection an advanced Search and Find will reveal.

Users can build queries based on glyph data you see by the collections view in Glyph List mode.

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

The name matches option is able to use regular expression. Regex can help you to create smart search queries and smart sets later on.

Examples:

*   **([a-z])\***

    lists all lowercase glyphs.

*   **([A-Z][a-z]\*)**

    lists all uppercase glyphs.

*   **[A-z]**

    lists all 52 uppercase and lowercase glyphs.

*   **[a-z](caron|cedilla|ogonek|commaaccent|grave|acute|dieresis)**

    lists all lowercase with those accents.

Save Set
--------

Users can save the query as a smart set. A smart set item will be created and will search the font dynamically based on the given query. The result will be adapted based on changes in the font.

Selection to Set
----------------

Save the selected glyphs in the Font Collection as smart set. This smart set will display glyphs based on a list of glyph names.

Read more: :ref:`displayModes`, :ref:`preferences`