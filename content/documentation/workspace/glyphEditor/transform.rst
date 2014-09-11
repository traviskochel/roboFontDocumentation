.. _transform:

Transform
=========

Transform let users transform selections or whole the glyph.
Transform is available when the Editing Tool is active.
To switch to transform mode can either be through the :ref:`applicationMenu` *Transform* or *command-T*
or you can create a Hot Key in the :ref:`preferences`.
Double click the selection will also switch into transform mode.

Double click outside the transform box will deactivate transform.

.. image:: /static/transform.png

Once users switched into transform mode it possible to translate, scale, rotate and skew the selection.

Translate
---------

Move the selection around. Translate is the default transform setting. (square corner points)

.. image:: /static/transformTranslate.png

.. cssclass:: doctable

+-------------------------------------------------------------+-------------------------------------------------------------------------------------+
| click + drag                                                | translate the selection                                                             |
+-------------------------------------------------------------+-------------------------------------------------------------------------------------+
| click + drag one of the four corners or their middle points | scale the selection                                                                 |
+-------------------------------------------------------------+-------------------------------------------------------------------------------------+
| drag + shift                                                | translate moves the selection on x, y or 45° axis                                   |
+-------------------------------------------------------------+-------------------------------------------------------------------------------------+
| drag + shift one of the four corners of their middle points | scale on x, y, 45° axis or proportional based on the transform box of the selection |
+-------------------------------------------------------------+-------------------------------------------------------------------------------------+

Scale
-----

Scale the selection. Activated when *command* is down. (diamond corner points)

.. image:: /static/transformScale.png

.. cssclass:: doctable

+--------------+------------------------------------------------------------------------------------+
| click + drag | start scaling the selection                                                        |
+--------------+------------------------------------------------------------------------------------+
| drag + shift | scale on x, y, 45° axis or proportional based on the bounding box of the selection |
+--------------+------------------------------------------------------------------------------------+

Skew
----

Skew the selection. Activated when *command + alt* is down. (triangular corner points)

.. image:: /static/transformSkew.png

.. cssclass:: doctable


+--------------+----------------------------------+
| click + drag | skew around the mouse down point |
+--------------+----------------------------------+
| drag + shift | skew on x, y or 45° axis         |
+--------------+----------------------------------+

Read more: :ref:`editingTool`, :ref:`inspector`

