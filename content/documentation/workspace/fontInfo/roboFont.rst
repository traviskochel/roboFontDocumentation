.. _fontInfoRoboFont:

RoboFont
========

.. image:: /static/fontInfoRoboFont.png

This sets preferences for UFO in RoboFont to deal with defaults for generating a font file from the UFO.

.. cssclass:: doctable

+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Decompose              | If checked, the font's components will be decomposed when a font is generated.                                                                                                                                                                     |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Remove Overlap         | If checked, overlap will be removed when the font is generated.                                                                                                                                                                                    |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Auto Hint              | If checked, the font will be auto hinted with the Adobe FDK autohinter (Postscript) or ttfautohint (TrueType–Only if installed in the system) using the settings from the :ref:`fontInfoHinting`.                                                  |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Release Mode           | If checked, will set the Adobe FDK in release mode when generating the font. This will turn on subroutinization (makes final OTF file smaller), applies your desired glyph order, and removes the word Development from the font's version string. |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Format                 | Which format to generate the font as: OTF, TTF, or PFA                                                                                                                                                                                             |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Italic Slant           | Offset Will shift your glyphs horizontally to the left during generating binaries. The number must have a negative value. This is mainly used during drawing italics with slanted metrics.                                                         |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Spline Conversion      | When changing between Cubic (Postscript) and Quadratic (TrueType) curves, the conversion can either preserve the number of points or preserve the curves (adding points as need be).                                                               |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Template Character Set | Set the default template character set for this font.                                                                                                                                                                                              |
+------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
