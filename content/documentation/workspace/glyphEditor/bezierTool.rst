.. _bezierTool:

Bezier Tool
===========

.. image:: /static/cursorDraw.png

A tool to draw contours.

.. cssclass:: doctable

+--------------------------+---------------------------------------------------------------------------------------------------+
| Mouse                                                                                                                        |
+--------------------------+---------------------------------------------------------------------------------------------------+
| click (no selection)     | add a point                                                                                       |
+--------------------------+---------------------------------------------------------------------------------------------------+
| alt click (no selection) | add a line segment                                                                                |
+--------------------------+---------------------------------------------------------------------------------------------------+
| click (on selection)     | when its the last point of an open contour the contour will become the main contour to add points |
+--------------------------+---------------------------------------------------------------------------------------------------+
| click shift              | adds point which is on the x, y or 45° of the previous on curve point                             |
+--------------------------+---------------------------------------------------------------------------------------------------+
| drag                     | adds bcp, they are all smooth                                                                     |
+--------------------------+---------------------------------------------------------------------------------------------------+
| drag shift               | move the bcps of the last added point on x, y or 45°                                              |
+--------------------------+---------------------------------------------------------------------------------------------------+
| drag alt                 | un-smooth the bcp                                                                                 |
+--------------------------+---------------------------------------------------------------------------------------------------+
| click alt command        | add a point on a contour                                                                          |
+--------------------------+---------------------------------------------------------------------------------------------------+
| move over starting point | can close the contour                                                                             |
+--------------------------+---------------------------------------------------------------------------------------------------+
| double click             | add a point and close the the contour                                                             |
+--------------------------+---------------------------------------------------------------------------------------------------+
| Key board                                                                                                                    |
+--------------------------+---------------------------------------------------------------------------------------------------+
| arrow keys               | move last added point by 1 unit                                                                   |
+--------------------------+---------------------------------------------------------------------------------------------------+
| arrow keys shift         | move last added point by 10 units                                                                 |
+--------------------------+---------------------------------------------------------------------------------------------------+
| arrow keys shift command | move last added point by 100 units                                                                |
+--------------------------+---------------------------------------------------------------------------------------------------+


