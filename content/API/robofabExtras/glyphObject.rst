RoboFab Glyph Extras
====================

.. class:: RGlyph()


    .. function:: addGuide((x, y), angle, name="")

        adds a guide at point x, y with angle and name
        returning the created guide

    .. function:: removeGuide(guide)

        will remove the guide from the glyph

    .. function:: addImage(path, offset=None)

        adds an image from path  with offset
        returning the created guide

    .. function:: clearImage()

        remove the image

    .. function:: removeOverlap()

        removes all overlaps in every glyphs

    .. function:: extremePoints()

        adds extremes points for every glyph

    .. function:: deselect()

        deselect everything

    .. function:: getLayer(layerName, clear=True)

        return the glyph for that layer, create a layer new layer if the layerName doesn't exists

    .. function:: copyToLayer(layerName, clear=True)

        copy the current layer to the a layer with the layerName

    .. function:: swapToLayer(layerName)

        swap current layer with the a layer with the layerName

    .. function:: flipLayers(layer1Name, layer2Name)

        flip layers

    .. function:: update()

        tell the UI that the glyph has changed directly

    .. function:: addObserver(observer, methodName, notification)

        adds an observer to the glyph that notifies the methodName of the observer for a given notification

    .. function:: removeObserver(observer, notification)

        removes the observer for the glyph for a  given notification

    .. attribute:: angledLeftMargin

        returns the angled left margin based on the italic angle in the font.info

    .. attribute:: angledRightMargin

        returns the angled right margin based on the italic angle in the font.info
    
    
    .. attribute:: getRayLeftMargin(y)

        returns the left margin at the value of y (similar to the beam)
        
    .. attribute:: getRayRightMargin(y)

        returns the right margin at the value of y (similar to the beam)

    .. attribute:: mark

        a tuple of 4 (r, g, b, a)

    .. attribute:: image

        the image object, if no image is set it will be None

    .. attribute:: guides

        a list of all the guides in the glyph

    .. attribute:: selection

        a list of selected points

    .. attribute:: selected

        returning True or False if yhe object is selected or not

:ref:`booleanGlyph`
-------------------

.. describe:: glyph | otherGlyph

    returns the union of the contours

.. describe:: glyph % otherGlyph

    returns the difference of the glyph contours

.. describe:: glyph & otherGlyph

    returns the intersection of the glyph contours

.. describe:: glyph ^ otherGlyph

    returns the xor of the glyph contours

.. toctree::
    :maxdepth: 2
    :titlesonly:
    :hidden:

    booleanGlyph
