.. _mojo.compile:

mojo.compile
============

::

    from mojo.compile import *


.. attribute:: FDKVersion

    Returns the version of the embedded FDK.

.. function:: makeotf(outputPath, outlineSourcePath=None, featuresPath=None, glyphOrderPath=None, menuNamePath=None, fontInfoPath=None, releaseMode=False)

    FDK makeotf

.. function:: checkOutlines(fontPath, removeOverlap=True, correctContourDirection=True)

    FDK checkOutlines

.. function:: otf2pfa(sourcePath, destinationPath)

    Convert a otf to pfa using FDK.

.. function:: otf2svg(sourcePath, destinationPath)

    Convert a otf to a svg font using FDK.

.. function:: autohint(fontPath)

    Autohint a postscript flavored font.

.. function:: hasTTFAutoHint()

    Return a boolean if ttfautohint is installed.

.. function:: ttfautohint(fontPath)

    Use ttf autohint if its locally installed to autohint a ttf file.

.. function:: stemHist(fontPath, userCurves=None, blueZones=False)

    Use FDK stemhist on a binary font. See stemHist help for details.

.. function:: setUseEmbeddedFDK(value)

    Set a boolean if RoboFont should use the embedded FDK.

.. function:: getUseEmbeddedFDK()

    Returns a boolean if RoboFont will use the embedded FDK.

.. function:: executeCommand(command, shell=False)

    Execute commands in the terminal. Commands must be a list of arguments.
    Optionally execute in the shell instead of inside RoboFont