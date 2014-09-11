.. _mojo.roboFont:

mojo.roboFont
=============

::

    from mojo.roboFont import *


.. class:: AllFonts()

    Returns a list of all open font objects, the list as some additional methods.

    .. function:: getFontsByStyleName(styleName)

        Returns all fonts with the given styleName.

    .. function:: getFontsByFamilyName(familyName)

        Returns all fonts with the given familyName.

    .. function:: getFontsByFamilyNameStyleName(familyName, styleName)

        Returns the font with the given familyName and styleName.

.. function:: CurrentFont()

    Returns the current font, will be None if no font is opened.

.. function:: CurrentGlyph()

    Returns the current glyph.

.. function:: NewFont(familyName=None, styleName=None, showUI=True)

    Creates a new font with the given *familyName* and *styleName*.
    Optionally you can create a new font without having a UI, this is much faster to do internal actions.

.. function:: OpenFont(path, showUI=True)

    oOens a UFO with a given path.
    Optionally you can create a new font without having a UI, this is much faster to do internal actions.

.. function:: RFont(path=None, showUI=True)
    :noindex:

    Creates a new font with the given path.
    Optionally you can create a new font without having a UI, this is much faster to do internal actions.

.. function:: RGlyph()
    :noindex:

    Creates a empty glyph object.

.. function:: RContour()

    Creates a empty contour object.

.. function:: RInfo()

    Creates a empty info object.

.. function:: RAnchor()

    Creates a empty anchor object.

.. function:: RGroups()

    Creates a empty group object.

.. function:: RFeatures()

    Creates a empty feature object.

.. function:: RComponent()

    Creates a empty component object.

.. function:: RKerning()

    Creates a empty kerning object.

.. function:: OpenWindow(controller, *args, **kwargs)

    Opens a window from the controller objects with args, and kwargs use this if you want RoboFont to deal with already opened versions of your window controller.

.. function:: CreateCursor(path, hotSpot=(4, 4))

    Creates a cursor object for image path with the given hotSpot.

.. attribute:: version

    Returns the version of RoboFont.