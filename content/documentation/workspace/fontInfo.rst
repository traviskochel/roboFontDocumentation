.. _fontInfo:

Font Info
=========

.. image:: /static/fontInfo.png

The Font Info sheet is an interface to edit font naming fields, vertical metrics and other font meta-data. It also holds RoboFont specific defaults that are local to the UFO. Many of the fields have a default value that only needs to be overridden if you have a need to. This means that for a simple font, all you need to fill in is Family Name and Style Name to get a working font. You only need to set the values where the default doesn't match your needs.

An example of this would be creating a eight weight font family where you want to style map the italics to the roman of each weight. To do so, you need to set four names in each font:

**My Font Light**

* Family Name: My Font
* Style Name: Light
* Style Map Family Name: My Font Light
* Style Map Style: Regular

**My Font Light Italic**

* Family Name: My Font
* Style Name: Light Italic
* Style Map Family Name: My Font Light
* Style Map Style: Italic

**My Font Book**

* Family Name: My Font
* Style Name: Book
* Style Map Family Name: My Font Book
* Style Map Style: Regular

**My Font Book Italic**

* Family Name: My Font
* Style Name: Book Italic
* Style Map Family Name: My Font Book
* Style Map Style: Italic

and so on.

Though RoboFont allows you to only set a few values, you have control of all values —down to setting FOND name info— if you need them:

.. toctree::
    :maxdepth: 2
    :titlesonly:

    fontInfo/general
    fontInfo/openType
    fontInfo/postscript
    fontInfo/miscallaneous
    fontInfo/roboFont

These values are derived from the Font Info section of the `UFO spec <http://unifiedfontobject.org>`_.