.. _mojo.UI:

mojo.UI
=======

::

    from mojo.UI import *

.. class:: AccordionView(posSize, descriptions, backgroundColor)

    A vanilla object hosting different kinds of other vanilla objects (like vanilla.List, vanilla.TextEditor, ....) in an accordion view.

    Initiate a AccordionView

    .. describe:: posSize

        a tuple of four, setting the size

    .. describe:: descriptions

        list of options for each item in the accordionView (see example)

    .. describe:: backgroundColor

        a NSColor object used as background color

.. showcode:: /RoboFontExamples/UI/customInspector.py

.. class:: HTMLView(posSize)

    Initiate a HTMLView

    .. describe:: posSize

        a tuple of four, setting the size

    .. function:: setHTMLPath(url)

        Set the url in the HTMLView

    .. function:: goBack()

        Go forward in the history of the HTMLView

    .. function:: goForward()

        Go forward in the history of the HTMLView

    .. function:: clearHistory()

        Clear the history of the HTMLView

.. class:: HelpWindow(htmlPath, title="help", developer=None, developerURL=None)

    Initiate a HelpWindow

    htmlPath: html help path

    .. describe:: title

        title of the help window

    .. describe:: developer

        a string with the name of the developer, optionally

    .. describe:: developerURL

        a URL link to the developer, optionally

    .. function:: set(htmlPath)

        set a html path in the HTMLView of the HelpWindow

.. showcode:: /RoboFontExamples/UI/simpleHelpWindow.py


.. class:: SmartSet(smartSet=dict())

    Initiate a smart set object

    .. describe:: smartSet

        a dictionary containing smart set data

        * **name**

            Set or get the smart set name.

        * **glyphNames**

            Set or get the a list of glyph names used by the smart set.

        * **query**

            Set or get a search query.


.. class:: MultiLineView(posSize, pointSize=150, lineHeight=50, doubleClickCallbak=None, applyKerning=None, bordered=False, hasHorizontalScroller=False, hasVerticalScroller=True, displayOptions=None, selectionCallback=None, menuForEventCallback=None)

    A multi glyph line view vanilla object, this is the same objects that is used to build a Space Center.
    Initiate a multi line view object:

    .. describe:: posSize

        a tuple of four, setting the size

    .. describe:: pointSize

        the initial point size, optionally

    .. describe:: lineHeight

        the initial lineHeight, , optionally

    .. describe:: doubleClickCallback

        callback for a double click event

    .. describe:: applyKerning

        enable kerning the view, optionally

    .. describe:: bordered

        set a border around the view

    .. describe:: hasHorizontalScroller

        set the horizontal scroller

    .. describe:: hasVerticalScroller

        set the vertical scroller

    .. describe:: displayOptions

        a dict with multi line view display options

    .. describe:: selectionCallback

        callback when a glyph get selected

    .. describe:: menuForEventCallback

        callback when a contextual menu will we used, required to return a NSMenu object

    .. function:: get()

        Returns all glyphs in the line view

    .. function:: set(glyphs)

        Sets a list of glyphs in the line view

    .. function:: setFont(font)

        The glyph line view needs a font as fallback and for font metrics

    .. function:: createNewLineGlyph()

        Returns a special glyph object that acts like a new line

    .. function:: createEmptyGlyph(name)

        Returns a special glyph object that acts like an empty glyph (use this as fallback when a glyph is not in the font)

    .. function:: setPointSize(pointSize)

        Sets the point size

    .. function:: setLineHeight(lineHeight)

        Sets the line height

    .. function:: setApplyKerning(value)

        Sets if kerning is applied in the line view

    .. function:: getDisplayStates()

        Returns a dict with all display options

    .. function:: setDisplayStates(options)

        Sets a dict of line view display options

    .. function:: setLeftToRight(value)

        Sets the reading direction of the glyph line view

.. showcode:: /RoboFontExamples/UI/multiLineView.py


.. function:: GlyphViewDisplaySettings(settings)

    Set display options for the current glyphview. Input as dict. These settings will be default for the glyphview. All options are: Fill, Stroke, Metrics, On Curve Points, Off Curve Points, Point Coordinates, Anchors, Curve Length, Blues, Family Blues, Rulers

.. function:: AllSpaceCenters()

    Get all open space centers

.. class:: CurrentSpaceCenter()

    Get the front most space center

    .. function:: get()

        returns a list of glyph names in the space center

    .. function:: getRaw()

        returns a string from the input of the space center

    .. function:: set(glyphNames)

        sets the list of glyphNames in the space center

    .. function:: setRaw(text)

        set a string in to the main input of the space center

    .. function:: getTracking()

        returns the tracking used

    .. function:: setTracking(value)

        set a tracking value between the glyphs

    .. function:: getLeftToRight()

        returns the reading direction

    .. function:: setLeftToRight(value)

        sets the reading direction

    .. function:: getPointSize()

        returns the point size

    .. function:: setPointSize(value)

        sets the points size

.. function:: SpaceCenterToPDF(path, spaceCenter=None)

    Saves the Space Center to a pdf with vector data, if a spaceCenter is not provided the CurrentSpaceCenter() will be used.

.. function:: AllGlyphWindows()

    Returns all open glyph windows.

.. function:: CurrentGlyphWindow()

    Returns the current glyph window.

.. function:: GlyphWindowToPDF(path, glyphWindow=None)

    Saves the Glyph Window to a pdf with vector data, if a Glyph Window is not provided the CurrentGlyphWindow() will be used.

.. function:: AllFontWindows()

    Returns all open font windows.

.. function:: CurrentFontWindow()

    Returns the current font window.

.. function:: OpenGlyphWindow(glyph=None, newWindow=False)

    Opens a new glyph window

    .. describe:: glyph

        a given glyph object

    .. describe:: newWindow

        open a new window, even if there is already a glyph window open

.. function:: OpenSpaceCenter(font, newWindow=False)

    Opens a new Space Center

    .. describe:: font

        a given font object

    .. describe:: newWindow

        open a new window, even if there is already a Space Center winow open

.. function:: OutputWindow()

    Returns the output window

    .. function:: write(text)

        Write a string in the output window

    .. function:: clear()

        Clears the output window

.. function:: SetCurrentGlyphByName(glyphName)

    Sets a glyph name in the current glyph editor

.. function:: SetCurrentLayerByName(layerName)

    Sets the current layer by a layerName in the current glyph editor

.. function:: UpdateCurrentGlyphView()

    Updates the current glyph editor

.. function:: SetCurrentLayerByName(layerName)

    Sets the current layer by layer name

.. function:: addSmartSet(smartSet, index=-1)

    Add a smart set object.
    Optionally set an index to insert the smart set object.

.. function:: removeSmartSet(smartSetName)

    Remove a smart set.

.. function:: getSmartSets()

    Get all current smart sets.

.. function:: setSmartSets(smartSets)

    Set a list of smart sets.

.. function:: setDefaultCharacterSet(characterSetName)

    Set the default character set by name as defined in the preferences.

.. function:: getDefaultCharacterSet()

    Get the current default character set name.

.. function:: addCharacterSet(characterSetName, glyphNames, useAsDefault=False)

    Add a character set with a name and a list of glyph names.

.. function:: removeCharacterSet(characterSetName)

    Remove a character set by name.

.. function:: getCharacterSets()

    Get all characeter sets as a dictionairy.

.. function:: setCharacterSets(characterSets)

    Set a dictionary of character sets.

.. function:: setMaxAmountOfVisibleTools(value)

    Set the maximum amount of visible tools in the toolbar.
    Must be in integer.

.. function:: getMaxAmountOfVisibleTools()

    Get the maximum amount of visible tools in the toolbar.

.. function:: setScriptingMenuNamingShortKey()

    Get the scripting menu names and shortkey dictionary.

.. function:: getScriptingMenuNamingShortKey(data)

    Set a scripting menu names and shortkey dictionary.

.. function:: setScriptingMenuNamingShortKeyForPath(path, preferredName, shortkey=None)

    Set the scripting menu names and shortkey dictionary.

.. function:: exportPreferences(path)

    Export all user preferences to a path.

.. function:: importPreferences(path)

    Import user preferences from a path.
