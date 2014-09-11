.. _savingFonts:

Saving Fonts
============

RoboFont can write several formats.

* `UFO files`_
* `Binary font files`_
* `Python files`_
* `Feature files`_

UFO files
---------

RoboFont can write `UFO1 <http://unifiedfontobject.org/versions/ufo1/index.html>`_ and `UFO2 <http://unifiedfontobject.org/versions/ufo2/index.html>`_ font files. It's recommended to use UFO2.

.. image:: /static/workflowSaveFont.png

As an option is possible to save images next to the UFO. This makes it easier to exchange UFO with :ref:`images`.

.. _generatingfontfiles:

Binary font files
-----------------

RoboFont can write:

* **otf**

  OpenType CFF flavored font

* **ttf**

  TrueType OpenType font

* **pfa**

  PostScript ASCII font

.. image:: /static/workflowGeneratingBinaries.png

.. cssclass:: doctable

+----------------+-------------------------------------------------------------------------------------------------------------------+
| otf pfa                                                                                                                            |
+----------------+-------------------------------------------------------------------------------------------------------------------+
| Decompose      | An OpenType CFF flavored font is always decomposed                                                                |
+----------------+-------------------------------------------------------------------------------------------------------------------+
| Remove Overlap | Remove overlap during generating the font                                                                         |
+----------------+-------------------------------------------------------------------------------------------------------------------+
| Autohint       | Enable FDK autohint                                                                                               |
+----------------+-------------------------------------------------------------------------------------------------------------------+
| Release Mode   | Removes the word 'Development' from the name table Version (see MakeOTFUserGuide.pdf)                             |
+----------------+-------------------------------------------------------------------------------------------------------------------+
| ttf                                                                                                                                |
+----------------+-------------------------------------------------------------------------------------------------------------------+
| Decompse       | Enable to decompose components                                                                                    |
+----------------+-------------------------------------------------------------------------------------------------------------------+
| Remove Overlap | Remove overlap during generating the font                                                                         |
+----------------+-------------------------------------------------------------------------------------------------------------------+
| Autohint       | Will be enable if `ttfautohint <http://www.freetype.org/ttfautohint/>`_ is installed on the users local computer. |
+----------------+-------------------------------------------------------------------------------------------------------------------+
| Release Mode   | Removes the word 'Development' from the name table Version (see MakeOTFUserGuide.pdf)                             |
+----------------+-------------------------------------------------------------------------------------------------------------------+

Enable 'Use MacRoman as the start of the glyph order' will force `MacRoman <http://en.wikipedia.org/wiki/Mac_OS_Roman>`_ to start the encoding with, otherwise it will take the order from the :ref:`fontcollection` sort.

Python files
------------

Saving python files from within the :ref:`scripting window <scripting>`.

Feature files
-------------

Saving feature files from within the :ref:`feature window <features>`.
