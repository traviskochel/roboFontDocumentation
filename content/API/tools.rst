.. _apiTools:

Tools
=====

.. image:: /static/glyphViewToolbar.png

You can add custom tools to RoboFont, by subclassing the `BaseEventTool`_ class or an existing core tool. RoboFont core tools are :ref:`bezierTool`, :ref:`editingTool`, :ref:`measurementTool` and :ref:`sliceTool`. They are available through the :ref:`mojo.events` module.

::

    from mojo.events import BaseEventTool
    ## or subclassing a core tool
    from mojo.events import BezierDrawingTool, EditingTool, MeasurementTool, SliceTool

This is an easy example, with most event callback. You need :meth:`installTool` to tell RoboFont you want to install in a new tool.
Custom tools can also be activated at start up through the :ref:`preferences`.

.. showcode:: /RoboFontExamples/tools/simpleTool.py


BaseEventTool
-------------

.. function:: tool.getGlyph()

    Returns the current glyph used by the tool

.. function:: tool.getNSView()

    Returns the current glyph view

.. function:: tool.getCurrentEvent()

    Returns the current NSEvent.

.. function:: tool.refreshView()

    updates the current glyph view

.. function:: tool.setCursor(cursor=None)

    Sets the cursor as current cursor (needs a NSCursor object), if None is given it will be return to default cursor of the tool

.. function:: tool.zoomRect(offset=None)

    zoom to a given rect

.. function:: tool.toggleTransformMode()

    Toggle the transform

.. function:: tool.getDefaultCursor()

    returns the default cursor for the tool, this must be overwritten

.. function:: tool.getToolbarIcon()

    returns the toolbar icon for the tool, this must be overwritten

.. function:: tool.mouseDown(point, clickCount)

    send a mouse down notification to the tool, with the mouse point in the and the clickCount

.. function:: tool.rightMouseDown(point, clickCount)

send a right mouse down notification to the tool, with the mouse point in the and the clickCount

.. function:: tool.modifyPoint(point)

    modify the point coordinates

    In the embedded tools this is used to modify the point when fe. on shiftDown

.. function:: tool.mouseMoved(point)

    send a mouse moved notification to the tool, be careful and optimize the code cause the mouse moves all the time

.. function:: tool.mouseDragged(point, delta)

    send a mouse dragged notification to the tool, the delta is the difference between the previous drag point

.. function:: tool.rightMouseDragged(point, delta)

    send a right mouse dragged notification to the tool, the delta is the difference between the previous drag point

.. function:: tool.mouseUp(point)

    send a mouse up notification to the tool

.. function:: tool.isDragging()

    returns a bools if the tool is in a dragging event

.. function:: tool.keyDown(event)

    send a key down notification to the tool, possible to get the pressed characters by event.characters()

.. function:: tool.keyUp(event)

    send a key up notification to the tool

.. function:: tool.modifiersChanged()

    send a modifiers changed notification to the tool, happens when shift, command, control, alt is changed

.. function:: tool.getModifiers()

    returns a dictionary with all the modifiers keys as bools. True when pressed down, keys are: shiftDown, commandDown, optionDown, controlDown

.. function:: tool.getArrowsKeys()

    returns a dictionary with all the arrows keys as bools. True when pressed down, keys are: up, down, left, right

Tools Menu methods
------------------

.. function:: tool.acceptMenuEditCallbacks()

    Overwrite this if you want your tool to accept menu callbacks.

.. function:: tool.selectAll()

    perform a select all in your tool, don't overwrite it if you don't want to do anything with it

.. function:: tool.selecteAllAlternate()

    perform a select all in your tool with alt key down, don't overwrite it if you don't want to do anything with it

.. function:: tool.deselectAll()

    perform a deselect all in your tool, don't overwrite it if you don't want to do anything with it

.. function:: tool.copy()

.. function:: tool.copyAsComponent()

.. function:: tool.cut()

.. function:: tool.delete()

.. function:: tool.paste()

.. function:: tool.additionContextualMenuItems()

    called when a contextual menu is created, it is required to return a list of tuples with a title string and a callback function
    example [("additional stuff", myObject.myAdditionMenuCallback), ]

Tools Draw Methods
------------------

.. function:: tool.draw(scale)

    draw in the glyph view

.. function:: tool.drawBackground(scale)

    draw in the background of the glyph view

.. function:: tool.drawPreview(scale)

    additional drawing in the glyph view while holding the glyph view preview key

.. function:: tool.drawInactive(scale, glyph, view)

    additional drawing in the glyph view when the glyph view is not active, the glyph will not be the current glyph, same for the view

.. function:: tool.drawBackgroundSelection(scale)

    draw in the background, should be related to a selection

.. function:: tool.drawSelection(scale, glyph, view)

    draw the selection for a glyph in a view

Space Center
------------

.. function:: tool.spaceCenterDraw(glyph, scale, selected, spaceCenter)

    draw in the space center for given glyph

.. function:: tool.spaceCenterKeyDown(glyph, event, spaceCenter)

    send a key down notification to the tool, possible to get the pressed characters by event.characters()

.. function:: tool.spaceCenterKeyUp(glyph, event, spaceCenter)

    send a key up notification to the tool

Tools Notifications Methods
---------------------------

.. function:: tool.viewWillChangeGlyph()

    the glyph in the current view will change

.. function:: tool.viewDidChangGlyph()

    the glyph in the current view did change

.. function:: tool.currentGlyphChanged()

    the current glyph in the app changed

.. function:: tool.preferencesChanged()

    the user defaults changed

.. function:: tool.becomeInactive()

    the tool becomes inactive

.. function:: tool.becomeActive()

    the tool becomes active

.. function:: tool.didUndo()

    a undo notification when the undo is already performed

.. function:: tool.glyphWindowWillOpen()

    a new glyph window will open

.. function:: tool.glyphWindowDidOpen()

    a new glyph window did open

.. function:: tool.glyphWindowWillClose()

    a glyph window will close

.. function:: tool.spaceCenterWillOpen()

    a new Space Center will open

.. function:: tool.spaceCenterDidOpen()

    a new Space Center did open

.. function:: tool.spaceCenterWillClose()

    a Space Center will close

.. function:: tool.fontWillOpen(font)

    a UFO will been opened

.. function:: tool.fontDidOpen(font)

    a UFO did open

.. function:: tool.newFontWillOpen(font)

    a new UFO will been created

.. function:: tool.newFontDidOpen(font)

    a new UFO is been created

.. function:: tool.binaryFontWillOpen(font, source, format)

    a binary font will open

    the source is the fontTools font object

.. function:: tool.fontWillClose(font)

    a UFO is been closed

.. function:: tool.applicationDidFinishLauching()

    the app is ready launching

.. function:: tool.applicationDidBecomeActive()

    the app becomes active

.. function:: tool.applicationWillResignActive()

    the app will resign being active

.. function:: tool.fontBecameCurrent(font)

    a font becomes active

.. function:: tool.fontResignCurrent(font)

    a font resigns being active

.. function:: tool.fontWillAutoSave(font)

    font will auto save

.. function:: tool.fontDidAutoSave(font)

    font did auto save

.. function:: tool.fontWillSave(font, path)

    font will save

.. function:: tool.fontDidSave(font, path)

    font did save

.. function:: tool.fontWillGenerate(font, format, path)

    font will generate to a binary format

.. function:: tool.fontDidGenerate(font, format, path)

    font did generate to a binary format

.. function:: tool.fontDidChangeExternally(font)

    An external change to the font has happend

Tools Attributes
----------------

.. attribute:: tool.allPointList

    A list of clicked and dragged points used by the tool

.. attribute:: tool.mouseDownPoints

    A list of clicked points used by the tool

.. attribute:: tool.shiftDown

    Bool if shift is down

.. attribute:: tool.commandDown

    Bool if command is down

.. attribute:: tool.optionDown

    Bool if option is down

.. attribute:: tool.controlDown

    Bool if control is down

.. attribute:: tool.spaceBarDown

    Bool if space is down

.. attribute:: tool.arrowKeysDown

    a dictionary of bools with keys: up, down, left, right

.. attribute:: tool.currentPoint

    returns the last points from the allPointsList

.. attribute:: tool.selection

    returns the current glyph selection object
