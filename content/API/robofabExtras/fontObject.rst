RoboFab Font Extras
===================

.. class::  RFont(path=None, showUI=True)

    Create a new font object has an optional *showUI*. *ShowUI* will toggle the creating of all interface objects around a font.

    .. function:: document()

        returns the related NSDocument

    .. function:: renameGlyph(oldName, newName, renameComponents=True, renameGroups=True, renameKerning=True)

        Rename a glyph in the font.
        Optionally the glyph can be renamed in all component references, groups and kerning.

    .. function:: generate(path, format, decompose=False, checkOutlines=False, autohint=False, releaseMode=False, glyphOrder=None, progressBar=None)

        Generate a font binary to the given path with the given format ("otf", "ttf", "pfa")

        Adding a progressBar object will show you the progress during compiling the font.

    .. function:: removeOverlap()

        removes all overlaps in every glyphs

    .. function:: extremePoints()

        adds extremes points for every glyph

    .. function:: testInstall()

        test instals the font, it returns the ID of the installed font on the os.

    .. function:: removeLayer(layerName)

        removes a complete layer, to create a layer just ask any glyph.getLayer("myLayerName")

    .. function:: addGuide((x, y), angle, name="")

        adds a guide at point x, y with angle and name
        returning the created guide

    .. function:: removeGuide(guide)

        Will remove the guide from the font

    .. function:: update()

        tell the UI that a font has changed directly

    .. function:: prepareUndo(undoTitle="")

        This marks to glyph to be ready that a action begins and it should be recorded to create an undo item when its done

    .. function:: performUndo()

        creates the undo item

    .. function:: setLayerDisplay(layerName, option, value)

        set display options for layers option: Fill, Stroke, Points, Coordinates

    .. function:: addObserver(observer, methodName, notification)

        adds an observer to the font that notifies the methodName of the observer for a given notification

    .. function:: removeObserver(observer, notification)

        removes the observer for the font for a  given notification

    .. attribute:: glyphOrder

        returns a list of glyph names in a specific order, it is possible to set the a list with a specific order in a font

    .. attribute:: layerOrder

        returns a list of layernames

    .. attribute:: guides

        a list of all the guides in the font

    .. attribute:: templateSelection

        next to the font.selection, which only contains glyphs in the font there is also a selection of template glyphs