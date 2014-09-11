Working With UFO's
==================

What is UFO?
------------

UFO stands for `Unified Font Object <http://unifiedfontobject.org>`_. It is a cross-platform, cross-application, human readable, future proof format for storing font data. The format is developed by Erik van Blokland, Tal Leming, and Just van Rossum. Because it is application neutral, several typeface design and font production applications use it natively; these are referred to as ‘UFO Tools’. UFO is a simple specification, one can rely on the ability to read/write the font data into the future, whatever the application landscape will look like then.

Advantages of UFO
-----------------

* An open and documented format
* UFO is XML: standards-based, future proof, easy to read and write
* Each glyph is stored separately – easy to access and track versions
* One can import/export UFO’s from `FontLab <http://www.fontlab.com/>`_, `Glyphs <http://glyphsapp.com/>`_, and `FontForge <http://fontforge.sourceforge.net/>`_


Possible disadvantage
---------------------

* Larger files (XML is verbose)

Converting font sources to UFO format
-------------------------------------

If you are switching to RoboFont from other applications, the first thing you’ll need to do is convert your font files to UFO.

From FontLab
------------

The easiest way to export UFOs from FontLab (version 4 or version 5) is by using Tal Leming’s UFOCentral python script. If you don’t have RoboFab installed, do so first. Install the linked script into your user/Library/Application Support/FontLab/Studio 5/Macros folder. After doing so, restart FontLab if it was running, and go to the macros panel. You should see ‘UFOCentral’ as an option now. With a VFB(s) open, run the script, selecting the Export checkbox. Be sure to select the ‘Format 2’ option (it is the default). The script will then export your VFB(s).

From Glyphs
-----------

Go to File ⇢ Export. Select UFO as the export option.

From FontForge
--------------

Select the UFO option from File ⇢ Save As.

UFO Tools
---------


Besides RoboFont, there are several other tools for working with UFO files, all doing different things. As of October 19th, 2011 here is a list:

* `MetricsMachine <http://tools.typesupply.com/metricsmachine.html>`_ : Tool for kerning
* `Prepolator <http://tools.typesupply.com/prepolator.html>`_ : Tool to check fonts for interpolation compatibility
* `Superpolator <http://superpolator.com/>`_: Tool to Superpolate fonts
* `RoundingUFO <http://roundingufo.typemytype.com/>`_: Tool to round the corners (and more) of glyphs
* `UFOStretch <http://UFOStretch.typemytype.com/>`_: Tool to transform, translate and interpolate a specific set of glyphs.