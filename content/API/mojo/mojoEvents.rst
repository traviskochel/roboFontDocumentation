.. _mojo.events:

mojo.events
===========

::

    from mojo.events import *

Imports useful helpers when building extensions and scripts requiring app event callbacks.

When subclassing or building tools on top of other tools you can find some embedded tools here.


.. function:: installTool(tool)

    install tool

.. function:: uninstallTool(tool)

    uninstall tool

.. function:: addObserver(observer, method, event)

    Adds an *observer* for an *event* to the observer *method*, callbacks will be send to the *method* of the *observer*.

.. function:: removeObserver(observer, event)

    Removes the *observer* for an *event*.

.. class:: BaseEventObserver

    The base class of an observer.

.. class:: BaseEventTool

    The base class of an Tool

.. class:: EditingTool

    A subclass-able :ref:`editingTool`

.. class:: MeasurementTool

    A subclass-able :ref:`measurementTool`

.. class:: SliceTool

    A subclass-able :ref:`sliceTool`

.. class:: BezierDrawingTool

    A subclass-able :ref:`bezierTool`
