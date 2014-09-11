.. _smartSets:

Smart sets
==========

The Font Collection can hold a number of Smart Sets. A Smart set is a list of saved search and find queries. Smart Sets can be organized in binders, ake groups.smar

.. image:: /static/smartSets.png

There are two kind of smart sets:

Query-based smart sets
----------------------

Displayed with a litle gear icon.

Based on a list of glyph names
------------------------------

Can display the amount of missing glyphs in the font.

Smart-sets based on glyph names are able to find missing glyphs, and create them by right-click on the smart set item. The counter indicates how many glyphs are missing from the total.

.. cssclass:: doctable

+----------------------------------------------+--------------------------------------------------------------------------------------------------------+
| click                                        | Set the seleted smart set as sub.                                                                      |
+----------------------------------------------+--------------------------------------------------------------------------------------------------------+
| double click                                 | Edit the smart set item, can either as a search query or as a list of glyph names.                     |
+----------------------------------------------+--------------------------------------------------------------------------------------------------------+
| right click (only for list based smart sets) | A contextual menu pops up displaying all missing glyph names and an option to create the missing ones. |
+----------------------------------------------+--------------------------------------------------------------------------------------------------------+
| click + alt                                  | Set all glyphs in the smart set as selected.                                                           |
+----------------------------------------------+--------------------------------------------------------------------------------------------------------+
| click + drag                                 | Rearrange the order of the smart sets.                                                                 |
+----------------------------------------------+--------------------------------------------------------------------------------------------------------+
| delete (del or backspace)                    | Remove the selected smart set.                                                                         |
+----------------------------------------------+--------------------------------------------------------------------------------------------------------+

Smart set Options
-----------------

.. cssclass:: doctable

+---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| Delete set                      | Delete the selected set.                                                                                                                        |
+---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| Export sets                     | Export the sets to a \*.roboFontSets file.                                                                                                      |
+---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| Load Sets                       | Loads a \*.roboFontSets file.                                                                                                                   |
+---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| Export To Group                 | Export the selected set to a group.                                                                                                             |
+---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| Create new set from glyph Names | Pops up a sheet where you can create a smart set based on a list of glyph names. (see Adding and deleting Glyphs for how to format glyph names) |
+---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| New Smart Group                 | Create a new 'binder', Smart Group to store and sort Smart Sets                                                                                 |
+---------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+

.. image:: /static/smartSetOptions.png

Right Click on a smart set
--------------------------

.. image:: /static/smartSetRightClick.png

Right click on a list based smart set will pop up a contextual menu if not all glyph are represented in the font. The pop up menu will provide a quick access to add the missing glyphs to the font. Double click a single glyph in the list will only generate the selected glyph.

Read more: :ref:`searchAndFind`, :ref:`addingAndDeletingGlyphs`