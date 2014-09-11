.. _images:

Images
======

Each layer can contain a single image. Drag & drop any *.png*, *.jpeg* or *.tiff* file on the glyph view and an image will be created. Working with multiple layers is a way to add multiple images.

The Editing Tool can handle editing the image.

.. image:: /static/imageEditing.png

The image data is not stored in the UFO file, only the path is stored. But there as saving options ‘save image next to the UFO’ that allows you to collect all images in a assets folder next the UFO.

Contextual menu
---------------

.. cssclass:: doctable

+---------------+--------------------------------------------------------------------------------------------+
| Brigtness     | Set the brightness of the selected image.                                                  |
+---------------+--------------------------------------------------------------------------------------------+
| Contrast      | Set the contrast of the selected image.                                                    |
+---------------+--------------------------------------------------------------------------------------------+
| Saturation    | Set the saturation of the selected image.                                                  |
+---------------+--------------------------------------------------------------------------------------------+
| Sharpness     | Set the Sharpness of the selected image.                                                   |
+---------------+--------------------------------------------------------------------------------------------+
| Black & White | Toggle the selected image to black & white.                                                |
+---------------+--------------------------------------------------------------------------------------------+
| Set Scale     | Opens a sheet that helps you to transform the image to the baseline, x-height. (see below) |
+---------------+--------------------------------------------------------------------------------------------+

Set Scale
---------

The Set Scale sheet helps you to transform the image in 3 clicks to the font horizontal metrics.

.. image:: /static/imageEditingSetScale.png

Define the following points just by clicking on the image:

* zero zero point
* define a base line
* define the height based either the x-height, cap-height, ascender or descender

The defined points are editable after the mouse down.

