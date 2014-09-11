.. _apiObservers:

Observers
=========

An observer has to be subscribed to an specific event. When the event happens the observer will get a notification.

.. showcode:: /RoboFontExamples/observers/simpleDrawAndObserver.py

Real live example drawing a reference to the current glyph in the Glyph View using the unicode value of the glyph:

.. showcode:: /RoboFontExamples/observers/drawReferenceGlyph.py

`More observers examples. <https://github.com/typemytype/RoboFontExamples/tree/master/observers>`_

Events
------

Any *observer* can subscriber to these events. The callback receives a dictionary object containing additional objects related to the send event.

Subscribe an *observer* with :meth:`addObserver`, remove them with :meth:`removeObserver`.

All notification dictionaries contains the following keys:

.. describe:: glyph

    The current/edited/active glyph.

.. describe:: tool

    The current tool.

.. describe:: view

    The current glyph view.


.. attribute:: applicationDidFinishLaunching

    Send when RoboFont did finish launching.

.. attribute:: applicationDidBecomeActive

    Send when RoboFont become the active application.

.. attribute:: applicationWillResignActive

    Send when RoboFont resigns being the active application.

.. attribute:: binaryFontWillOpen

    Send when a binary font will open.

    .. describe:: font

        The font object.

    .. describe:: source

        The fontTools source object.

    .. describe:: format

        The format of the source font.

.. attribute:: fontWillSave

    Send when a font will save.

    .. describe:: font

        The font object.

    .. describe:: path

        The path where the font will be saved.

.. attribute:: fontDidSave

    Send when a font is done saving.

    .. describe:: font

        The font object.

    .. describe:: path

        The path where the font did save.

.. attribute::  fontWillClose

    Send when a font will close.

    .. describe:: font

        The font object.

.. attribute:: newFontWillOpen

    Send when a new font will open.

    .. describe:: font

        The font object.

.. attribute:: newFontDidOpen

    Send when a new font did open.

    .. describe:: font

        The font object.

.. attribute:: fontWillOpen

    Send when a font will open.

    .. describe:: font

        The font object.

.. attribute:: fontDidOpen

    Send when a font did open.

    .. describe:: font

        The font object.

.. attribute:: fontWillAutoSave

    Send when a font will auto save.

    .. describe:: font

        The font object.

    .. describe:: path

        The path where the font did autosave.

.. attribute:: fontDidAutoSave

    Send when a font did auto save.

    .. describe:: font

        The font object.

    .. describe:: path

        The path where the font did autosave.

.. attribute:: fontDidChangeExternally

    Send when a font did change externally, outside RoboFont.

    .. describe:: font

        The font object.

.. attribute:: fontWillGenerate

    Send when a font will generate.

    .. describe:: font

        The font object.

    .. describe:: format

        The format of the generated font.

    .. describe:: path

        The path where the binary font will save.

.. attribute:: fontDidGenerate

    Send when a font did generate.

    .. describe:: font

        The font object.

    .. describe:: format

        The format of the generated font.

    .. describe:: path

        The path where the binary font will save.

.. attribute:: currentGlyphChanged

    Send when the current glyph changed, this can be either in the glyph view or in the font overview.

.. attribute:: viewWillChangeGlyph

    Send when the glyph view will switch to an other glyph.

.. attribute:: viewDidChangeGlyph

    Send when the glyph view did switch to an other glyph.

.. attribute:: glyphWindowWillOpen

    Send when a glyph window will open.

    .. describe:: window

        The glyph window that will open.

.. attribute:: glyphWindowDidOpen

    Send when a glyph window did open.

    .. describe:: window

        The glyph window that did open.

.. attribute:: glyphWindowWillClose

    Send when a glyph window will close.

    .. describe:: window

        The glyph window that will close.

.. attribute:: spaceCenterWillOpen

    Send when a space center will open.

    .. describe:: window

        The space center window that will open.

.. attribute:: spaceCenterDidOpen

    Send when a space center did open.

    .. describe:: window

        The space center window that did open.

.. attribute:: spaceCenterWillClose

    Send when a space center will close.

    .. describe:: window

        The space center window that will close.

.. attribute:: transformChanged

    Send when a transformation is applied to a glyph.

    .. describe:: scale

    .. describe:: translate

    .. describe:: rotate

    .. describe:: skew

    .. describe:: repeatMatrix

.. attribute:: extensionDidGenerate

    Send when an extension did generate.

    .. describe:: path

        The path to the extension.

.. attribute:: spaceCenterDraw

    Send when a space center draws a glyph, this can happen a lot so be care full.

    .. describe:: scale

        The drawing scale.

    .. describe:: spaceCenter

        The space center.

    .. describe:: selected

        A bool if the glyph is selected in the space center.

.. attribute:: spaceCenterKeyDown

    Send on a key down in a space center.

    .. describe:: event

        The NSEvent object.

    .. describe:: spaceCenter

        The space center.

.. attribute:: spaceCenterKeyUp

    Send on a key up in space center.

    .. describe:: event

        The NSEvent object.

    .. describe:: spaceCenter

        The space center.

.. attribute:: drawPreview

    Send when the glyph view draws a preview.

    .. describe:: scale

.. attribute:: drawBackground

    Send when the glyph view draws the background, before the actual glyph data.

    .. describe:: scale

.. attribute:: draw

    Send when the glyph view draw the glyph data.

    .. describe:: scale

.. attribute:: drawInactive

    Send when the glyph view draw when the glyph window is not the active one.

    .. describe:: scale

.. attribute:: mouseDown

    Send on mouse down in the glyph view.
    point the point coordinates of the mouse in the glyph coordinate system

    .. describe:: clickCount

        The click count.

    .. describe:: offset

        Offset of the zero zero point in the glyph view.

    .. describe:: event

        The NSEvent object.

.. attribute:: rightMouseDown

    Send on right mouse down in the glyph view.

    .. describe:: point

        The point coordinates of the mouse in the glyph coordinate system.

    .. describe:: event

        The NSEvent object.

.. attribute:: mouseDragged

    Send on a mouse drag in the glyph view.

    .. describe:: point

        The point coordinates of the mouse in the glyph coordinate system.

    .. describe:: offset

        Offset of the zero zero point in the glyph view.

    .. describe:: delta

        Delta of the drag form the first click.

    .. describe:: event

        The NSEvent object.

.. attribute:: rightMouseDragged

    Send on a right mouse drag in the glyph view.

    .. describe:: point

        The point coordinates of the mouse in the glyph coordinate system.

    .. describe:: offset

        Offset of the zero zero point in the glyph view.

    .. describe:: event

        The NSEvent object.

.. attribute:: mouseUp

    Send on a mouse up in the glyph view.

    .. describe:: point

        The point coordinates of the mouse in the glyph coordinate system.

    .. describe:: offset

        Offset of the zero zero point in the glyph view.

    .. describe:: event

        The NSEvent object.

.. attribute:: keyDown

    Send on a key down in the glyph view.

    .. describe:: event

        The NSEvent object.

.. attribute:: keyUp

    Send on a key up in the glyph view.

    .. describe:: event

        The NSEvent object.

.. attribute:: modifiersChanged

    Send when the modifier changed in the glyph view (command, alt, control and shift keys)

    .. describe:: event

        The NSEvent object.

.. attribute:: toggleTransformMode

    Send when the glyph view toggles from or out the transform mode.

.. attribute:: acceptMenuEditCallbacks

    Send when a contextual menu is been build.

    .. describe:: item

        A menu item.

.. attribute:: selectAll

    Send on select all in the glyph view.

.. attribute:: deselectAll

    Send on deselect all in the glyph view.

.. attribute:: selectAllAlternate

    Send on select all alternate in the glyph view.

.. attribute:: copy

    Send on copy in the glyph view.

.. attribute:: copyAsComponent

    Send on copy as component in the glyph view.

.. attribute:: cut

    Send on cut in the glyph view.

.. attribute:: delete

    Send on delete in the glyph view.

.. attribute:: paste

    Send on paste in the glyph view.