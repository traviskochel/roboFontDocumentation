.. _editingTool:

Editing Tool
============

.. image:: /static/cursorEdit.png

A tool to edit existing glyph data.

.. cssclass:: doctable

+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Point Selection                                                                                                                                                                               |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| click (no selection)                          | deselect all                                                                                                                                  |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| click drag (no selection)                     | select all points in selection marque                                                                                                         |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| click point                                   | select point                                                                                                                                  |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| click shift                                   | toggle selected points                                                                                                                        |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| click drag                                    | moves the selected points                                                                                                                     |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| click drag shift                              | moves the selected points on x, y or 45° axis                                                                                                 |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| click drag alt                                | if the points does not have a bcp it creates one other wise it will un-smooth the point and only move the on curve point                      |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| click drag control                            | copies the selection while dragging                                                                                                           |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| click drag alt (single bcp selection)         | bcp becomes not smooth                                                                                                                        |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| click drag alt command (single bcp selection) | bcp becomes smooth and the bcp values are mirror on the other bcp is there is one.                                                            |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| command drag smooth point                     | * if selection is an oncurve point it will be moved over the handles                                                                          |
|                                               | * if off curve point the handle will be moved in the same direction as the handle                                                             |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| join / close contour                          | if contour is open and first or last on curve point is dragged on top of another first or last on curve point the contour are joined or close |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| tab                                           | jump to the next oncurve point                                                                                                                |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Segment Selection                                                                                                                                                                             |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| click                                         | select segment                                                                                                                                |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| click shift                                   | add segment to selection                                                                                                                      |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| click drag (single segment selection)         | move the selected segments around                                                                                                             |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| click drag alt (single segment selection)     | * for line segment: create curve segment (adds two bcps)                                                                                      |
|                                               | * for curve semgent: drag the handles around. (this will un-smooth your on curve points)                                                      |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| click drag command (single segment selection) | * for line segment: move the selected segment around                                                                                          |
|                                               | * for curve segments: the bcp are following the handle direction                                                                              |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| click drag shift (single segment selection)   | all points fixed are on x, y or 45°, works also with alt and command down                                                                     |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| click drag control                            | copy the selected segment during drag                                                                                                         |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| command alt (no selection)                    | add point on contour                                                                                                                          |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Contour Selection                                                                                                                                                                             |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| double click                                  | select contour                                                                                                                                |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| click drag (in/on selection)                  | move the selection                                                                                                                            |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| click drag shift (in/on selection)            | move the selection on x, y or 45°                                                                                                             |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Component Selection                                                                                                                                                                           |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| click                                         | select the component                                                                                                                          |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| click shift                                   | toggles the component selection                                                                                                               |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| drag                                          | move the components around                                                                                                                    |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| drag shift                                    | move the components on x, y or 45°                                                                                                            |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| triple click (in the component)               | to the base glyph to edit                                                                                                                     |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+

Copy Paste
----------

.. cssclass:: doctable

+----------------------+---------------------------------------------------+
| Copy                                                                     |
+----------------------+---------------------------------------------------+
| selection            | copies the selection from the current glyph       |
+----------------------+---------------------------------------------------+
| Paste                                                                    |
+----------------------+---------------------------------------------------+
| from glyph editor    | paste the copied selection into the current glyph |
+----------------------+---------------------------------------------------+
| from font collection | paste the copied selection into the current glyph |
+----------------------+---------------------------------------------------+
| from illustrator     | paste the copied selection into the current glyph |
+----------------------+---------------------------------------------------+

Contextual Menus
----------------

.. cssclass:: doctable

+------------------------------------------+------------------------------------------------------+
| Right Click no selection                                                                        |
+------------------------------------------+------------------------------------------------------+
| Add Component                            | Opens an Add Component sheet.                        |
+------------------------------------------+------------------------------------------------------+
| Add Anchors                              | Opens an Add Anchor sheet.                           |
+------------------------------------------+------------------------------------------------------+
| Reverse                                  | Reverse the whole glyph.                             |
+------------------------------------------+------------------------------------------------------+
| Remove Overlap                           | Removes overlaps the whole glyph.                    |
+------------------------------------------+------------------------------------------------------+
| Auto Contour order                       | Tries to order the contours.                         |
+------------------------------------------+------------------------------------------------------+
| Add Extreme Points                       | Adds extreme points.                                 |
+------------------------------------------+------------------------------------------------------+
| Corrent Directions (PS)                  | Corrects contour direction to postscript directions. |
+------------------------------------------+------------------------------------------------------+
| Corrent Directions (TT) + alt            | Corrects contour direction to truetype directions.   |
+------------------------------------------+------------------------------------------------------+
| Lock Guides                              | Locks all guides in RoboFont.                        |
+------------------------------------------+------------------------------------------------------+
| Lock Images                              | Locks all images in RoboFont.                        |
+------------------------------------------+------------------------------------------------------+
| Copy To Layer                            | List all available layers to copy to.                |
+------------------------------------------+------------------------------------------------------+
| Copy To Layer + alt                      | List all available layers to swap to.                |
+------------------------------------------+------------------------------------------------------+
| Right Click with selection                                                                      |
+------------------------------------------+------------------------------------------------------+
| Reverse                                  | Reverse the only the selected contours.              |
+------------------------------------------+------------------------------------------------------+
| Remove Overlap                           | Removes overlaps only the selected contours.         |
+------------------------------------------+------------------------------------------------------+
| Labels                                   | Add labels to the selected points.                   |
+------------------------------------------+------------------------------------------------------+
| Right Click on point                                                                            |
+------------------------------------------+------------------------------------------------------+
| Break Contour                            | Breaks the contour at the selected point.            |
+------------------------------------------+------------------------------------------------------+
| Reverse                                  | Reverse the whole glyph.                             |
+------------------------------------------+------------------------------------------------------+
| Set Start Point                          | Set the selected point as starting point.            |
+------------------------------------------+------------------------------------------------------+
| Right Click glyph contains a component                                                          |
+------------------------------------------+------------------------------------------------------+
| Component -> Go to                       | Jump to glyph with.                                  |
+------------------------------------------+------------------------------------------------------+
| Component -> Go to + alt                 | Decompose component with base glyph.                 |
+------------------------------------------+------------------------------------------------------+
| Component -> Decompose selected          | Decompose selected components.                       |
+------------------------------------------+------------------------------------------------------+
| Component -> Decompose All               | Decompose all components.                            |
+------------------------------------------+------------------------------------------------------+
| Right Click on Anchor                                                                           |
+------------------------------------------+------------------------------------------------------+
| Name                                     | Set name for the selected anchor.                    |
+------------------------------------------+------------------------------------------------------+
| Right Click on Guide (see :ref:`guides`)                                                        |
+------------------------------------------+------------------------------------------------------+
| Right Click on Image (see :ref:`images`)                                                        |
+------------------------------------------+------------------------------------------------------+
