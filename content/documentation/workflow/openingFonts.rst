.. _openingFonts:

Opening Fonts
=============

RoboFont can read several file formats.

* `UFO files`_
* `Binary font files`_
* `Python files`_
* `Feature files`_

UFO files
---------

RoboFont can read UFO1 and UFO2 font files.

Opening a UFO can either go by double clicking the file, only if RoboFont is the preferred UFO editor off course :) or drag the file on the app icon or through the 'Open' application menu.

Binary font files
-----------------

RoboFont can read:

* **otf**

  OpenType CFF flavored font

* **ttf**

  TrueType OpenType font

* **pfa**

  PostScript ASCII font

* **pfb**

  PostScript binary font

* **WOFF**

  Web Open Font Format

* **ttx**

  fontTools xml font

* **Font Suitecase**

  Extremely Old mac font format


RoboFont will read all glyphs and their corresponding outlines and tries to read the font info.

RoboFont will not read features from *.otf* and *.ttf* OpenType fonts.

Python files
------------

RoboFont can be your preferred python editor. It opens all python files (*.py*) in the :ref:`scripting window <scripting>`.

A folder with several python files can be dropped on RoboFont's app icon to open the folder in a scripting window.

Feature files
-------------

RoboFont read and writes `Adobe Feature files <http://www.adobe.com/devnet/opentype/afdko/topic_feature_file_syntax.html>`_ (*.fea*) natively. Opening a feature file will open a :ref:`features window <features>`. This Window is not attached to a specific font.

To save feature files (*.fea*) from a font choose "Export Feature" from the file menu (see :ref:`applicationMenu`)

Import Warnings
---------------

Groups with a ' (quote)
^^^^^^^^^^^^^^^^^^^^^^^

.. image:: /static/workflowWarningGroups.png

RoboFont will warn users when they have groups exported from FontLab with a \' (quote) master glyph.

A warning is been printed in the :ref:`outputWindow`.

.. image:: /static/workflowWarningGroupsResult.png

Truetype font or font with quadratic curves
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: /static/workflowWarningTrueTypeWithQuads.png

RoboFont can handle quadratic curves but with the limitation there are only two off curve points for each segment. During import RoboFont checks and converts all quadratic segments to two off curves points segments.

The warning sheet can be hidden for future display.

Mixed curve description
^^^^^^^^^^^^^^^^^^^^^^^

.. image:: /static/workflowWarningMixedCurves.png

RoboFont doesn't not allow mixed curve descriptions. Mixing bezier curves and truetype splines is in general not a good idea. RoboFont provides a warning sheet that allows users to choose to which curve description they want to change.

Preferred curve description can be set in the :ref:`preferences`.

Import errors
^^^^^^^^^^^^^

If something goes wrong during importing RoboFont show a nice traceback. This can either be the UFO is badly written or a font file isn't readable any more.

Read more: :ref:`preferences`

Revert
------

It is possible to revert to a save data on disk with 'revert'. Users can select parts to revert, this ignore other data.

.. image:: /static/workflowRevert.png

