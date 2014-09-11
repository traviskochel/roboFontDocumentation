.. _mojo.canvas:

mojo.canvas
===========

::

    from mojo.canvas import Canvas


A vanilla object that sends all user input events to a given delegate.

.. class:: Canvas(posSize, delegate=None, canvasSize=(1000, 1000), acceptsMouseMoved=False, hasHorizontalScroller=True, hasVerticalScroller=True, autohidesScrollers=False, backgroundColor=None, drawsBackground=True)

    All optional delegate methods

    .. function:: draw()

        Callback when the canvas get drawn.

    .. function:: becomeFirstResponder(event)

        Callback when the canvas becomes the first responder, when it starts to receive user interaction callbacks.

    .. function:: resignFirstResponder(event)

        Callback when the canvas resigns the first responder, when the canvas will not longer receive user interaction callbacks.

    .. function:: mouseDown(event)

        Callback when the user hit the canvas with the mouse.

    .. function:: mouseDragged(event)

        Callback when the user drag the mouse around in the canvas.

    .. function:: mouseUp(event)

        Callback when the user lifts up the mouse from the canvas.

    .. function:: mouseMoved(event)

        Callback when the user moves the mouse in de canvas. Be careful this is called frequently. (only when *accepsMouseMoved* is set *True*)

    .. function:: rightMouseDown(event)

        Callback when the user clicks inside the canvas with the right mouse button.

    .. function:: rightMouseDragged(event)

        Callback when the users is dragging in the canvas with the right mouse button down.

    .. function:: rightMouseUp(event)

        Callback when the users lift up the right mouse button from the canvas.

    .. function:: keyDown(event)

        Callback when the users hits a key.

        The event object has a *characters()* method returns the pressed character key.

    .. function:: keyUp(event)

        Callback when the users lift up the key.

    .. function:: flagChanged(event)

        Callback when the users changed a modifier flag: *command*, *shift*,  *control*,  alt

.. showcode:: /RoboFontExamples/canvas/simpleCanvas.py