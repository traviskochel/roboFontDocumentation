.. _fontInfoOpenType:

OpenType
========

OpenType specific font info. For further information on any of these options, consult the `OpenType specification <http://www.microsoft.com/typography/otspec/default.htm>`_.

* `head table`_
* `name table`_
* `hhea table`_
* `vhea table`_
* `OS/2 table`_

head table
----------

.. image:: /static/fontInfoOpenTypeHead.png

.. cssclass:: doctable

+---------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| Option        | Default            | Description                                                                                                                                  |
+===============+====================+==============================================================================================================================================+
| created       | Current date/time. | The creation date of the font.                                                                                                               |
+---------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| lowestRecPPEM | 6                  | Smallest readable size in pixels. Corresponds to the OpenType head table lowestRecPPEM field.                                                |
+---------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| flags         | Off                | A list of flags one can set based on the OpenType specification. Most of these flags, though not all, are for TrueType hinting. Options are: |
|               |                    |                                                                                                                                              |
|               |                    | * Flag 0: Baseline for font at y=0                                                                                                           |
|               |                    | * Flag 1:  Left side-bearing point at x=0                                                                                                    |
|               |                    | * Flag 2:  Instructions may depend on point size                                                                                             |
|               |                    | * Flag 3: Force ppem to integer values for all internal scaler math                                                                          |
|               |                    | * Flag 4: Instructions may alter advance width                                                                                               |
|               |                    | * Flag 11: Font data is "lossless"                                                                                                           |
|               |                    | * Flag 12: Font converted (produce compatible metrics)                                                                                       |
|               |                    | * Flag 13: Font optimized for ClearType                                                                                                      |
+---------------+--------------------+----------------------------------------------------------------------------------------------------------------------------------------------+

name table
----------

.. image:: /static/fontInfoOpenTypeName.png

.. cssclass:: doctable

+--------------------------+-----------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| Option                   | default                                                                                                         | Description                                                                  |
+==========================+=================================================================================================================+==============================================================================+
| Preferred Family Name    | Family Name                                                                                                     | Preferred family name. Corresponds to the OpenType name table name ID 16.    |
+--------------------------+-----------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| Preferred Subfamily Name | Style Name                                                                                                      | Preferred subfamily name. Corresponds to the OpenType name table name ID 17. |
+--------------------------+-----------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| Compatible Full Name     | Style Map Family Name followed by Style Map Style Name. If the Style Map Style Name is Regular, it is not used. | Compatible full name. Corresponds to the OpenType name table name ID 18.     |
+--------------------------+-----------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| WWS Family Name          | Not Set                                                                                                         | WWS family name. Corresponds to the OpenType name table name ID 21.          |
+--------------------------+-----------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| WWS Subfamily Name       | Not set                                                                                                         | WWS Subfamily name. Corresponds to the OpenType name table name ID 22.       |
+--------------------------+-----------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| Version                  | Version Major followed by Version Minor in the from of 0.000                                                    | Version string. Corresponds to the OpenType name table name ID 5.            |
+--------------------------+-----------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| Unique ID                | A string that is: OpenType Version;OS/2 Vender ID;Style Map Family Name followed by Style Map Style Name        | Unique ID string. Corresponds to the OpenType name table name ID 3.          |
+--------------------------+-----------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| Description              | Not set                                                                                                         | Description of the font. Corresponds to the OpenType name table name ID 10.  |
+--------------------------+-----------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| Sample Text              | Not set                                                                                                         | Sample text. Corresponds to the OpenType name table name ID 20.              |
+--------------------------+-----------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+

hhea table
----------

.. image:: /static/fontInfoOpenTypeHhea.png

.. cssclass:: doctable

+----------------+--------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option         | Default                              | Description                                                                                                                                                       |
+================+======================================+===================================================================================================================================================================+
| Ascender       | Units Per Em value + Descender value | Ascender value. Corresponds to the OpenType hhea table Ascender field.                                                                                            |
+----------------+--------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Descender      | Descender value                      | Descender value. Corresponds to the OpenType hhea table Descender field.                                                                                          |
+----------------+--------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LineGap        | 200                                  | Line gap value. Corresponds to the OpenType hhea table LineGap field.                                                                                             |
+----------------+--------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| caretSlopeRise | 1                                    | Used to set the slope of the text cursor (rise/run). Use 1 for vertical. Corresponds to the OpenType hhea table caretSlopeRise field.                             |
+----------------+--------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| caretSlopeRun  | 0                                    | Used in conjunction with caretSlopeRise. Use 0 for vertical. Corresponds to the OpenType hhea table caretSlopeRun field.                                          |
+----------------+--------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| caretOffset    | 0                                    | The amount to shift a slanted highlight to produce the best appearance. Set to 0 for non-slanted fonts. Corresponds to the OpenType hhea table caretOffset field. |
+----------------+--------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

vhea table
----------

.. image:: /static/fontInfoOpenTypeVhea.png

.. cssclass:: doctable

+-------------------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option            | default | Description                                                                                                                                                                                                                                                           |
+===================+=========+=======================================================================================================================================================================================================================================================================+
| vertTypoAscender  | Not set | Vertical ascender value. Distance from the centerline to the previous line's descent. Corresponds to the OpenType vhea table vertTypoAscender field.                                                                                                                  |
+-------------------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| vertTypoDescender | Not set | Vertical descender value. Distance from the centerline to the next line's ascent. Corresponds to the OpenType vhea table vertTypoDescender field.                                                                                                                     |
+-------------------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| vertTypoLineGap   | Not set | Line gap value. Corresponds to the OpenType vhea table vertTypoLineGap field.                                                                                                                                                                                         |
+-------------------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| caretSlopeRise    | Not set | Vertical caret slope rise value. A value of 0 for the rise and a value of 1 for the run specifies a horizontal caret. A value of 1 for the rise and a value of 0 for the run specifies a vertical caret. Corresponds to the OpenType vhea table caretSlopeRise field. |
+-------------------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| caretSlopeRun     | Not set | Vertical caret slope run value. See the caretSlopeRise field. Corresponds to the OpenType vhea table caretSlopeRun field.                                                                                                                                             |
+-------------------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| caretOffset       | Not set | Vertical caret offset value. The amount to shift a slanted highlight to produce the best appearance. Set to 0 for non-slanted fonts. Corresponds to the OpenType vhea table caretOffset field.                                                                        |
+-------------------+---------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

OS/2 table
----------

.. image:: /static/fontInfoOpenTypeOS.png

.. cssclass:: doctable

+---------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option              | Default                                                             | Description                                                                                                                                                                                                                    |
+=====================+=====================================================================+================================================================================================================================================================================================================================+
| usWidthClass        |                                                                     | Width class value. Can be Ultra-condensed, Extra-condensed, Condensed, Semi-Condensed, Medium (normal), Semi-expanded, Expanded, Extra-expanded, or Ultra-expanded. Corresponds to the OpenType OS/2 table usWidthClass field. |
+---------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| usWeightClass       |                                                                     | Weight class value. Must be a positive integer. Corresponds to the OpenType OS/2 table usWeightClass field.                                                                                                                    |
+---------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| fsSelection         | Nothing Set                                                         | Options are:                                                                                                                                                                                                                   |
|                     |                                                                     |                                                                                                                                                                                                                                |
|                     |                                                                     | * 1 UNDERSCORE: Characters are underscored                                                                                                                                                                                     |
|                     |                                                                     | * 2 NEGATIVE: Characters have their foreground and background reversed                                                                                                                                                         |
|                     |                                                                     | * 3 OUTLINED: Outlined characters                                                                                                                                                                                              |
|                     |                                                                     | * 4 STRIKEOUT: Characters are over-struck                                                                                                                                                                                      |
|                     |                                                                     | * 7 USE_TYPO_METRICS: Use OS/2 Typo values for ascender, descender, and line gap                                                                                                                                               |
|                     |                                                                     | * 8 WWS: Font has name table strings consistent with a weight/width/slope family without requiring the WWS name values                                                                                                         |
|                     |                                                                     | * 9 OBLIQUE: Font is oblique                                                                                                                                                                                                   |
+---------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| achVendID           |                                                                     | Four character identifier for the creator of the font. Corresponds to the OpenType OS/2 table achVendID field.                                                                                                                 |
+---------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| fsType              | No embedding restrictions                                           | The allowed type of embedding for the font. Options are:                                                                                                                                                                       |
|                     |                                                                     |                                                                                                                                                                                                                                |
|                     |                                                                     | * No embedding restrictions                                                                                                                                                                                                    |
|                     |                                                                     | * No embedding                                                                                                                                                                                                                 |
|                     |                                                                     | * Only preview and print embedding allowed                                                                                                                                                                                     |
|                     |                                                                     | * Editable embedding allowed                                                                                                                                                                                                   |
|                     |                                                                     | * Additionally, one can choose if they wish to allow subsetting and/or only bitmap embedding.                                                                                                                                  |
+---------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ulUnicodeRange      |                                                                     | A list of supported Unicode ranges in the font. Corresponds to the OpenType OS/2 table ulUnicodeRange1, ulUnicodeRange2, ulUnicodeRange3 and ulUnicodeRange4 fields.                                                           |
+---------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ulCodePageRange     |                                                                     | A list of supported code page ranges in the font. Corresponds to the OpenType OS/2 table ulCodePageRange1 and ulCodePageRange2 fields.                                                                                         |
+---------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| sTypoAscender       | Units Per Em value + Descender value                                | Ascender value. Corresponds to the OpenType OS/2 table sTypoAscender field.                                                                                                                                                    |
+---------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| sTypoDescender      | Descender value                                                     | Descender value. Must be 0 or a negative number. Corresponds to the OpenType OS/2 table sTypoDescender field.                                                                                                                  |
+---------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| sTypoLineGap        | 200                                                                 | Line gap value. Corresponds to the OpenType OS/2 table sTypoLineGap field.                                                                                                                                                     |
+---------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| usWinAscent         | Maximum y value of the font. If not available, the Ascender value.  | Ascender value. Corresponds to the OpenType OS/2 table usWinAscent field.                                                                                                                                                      |
+---------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| usWinDescent        | Minimum y value of the font. If not available, the Descender value. | Descender value. Must be 0 or a positive number. Corresponds to the OpenType OS/2 table usWinDescent field.                                                                                                                    |
+---------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ySubscriptXSize     | Adobe FDK will calculate                                            | Subscript horizontal font size. Corresponds to the OpenType OS/2 table ySubscriptXSize field.                                                                                                                                  |
+---------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ySubscriptYSize     | Adobe FDK will calculate                                            | Subscript vertical font size. Corresponds to the OpenType OS/2 table ySubscriptYSize field.                                                                                                                                    |
+---------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ySubscriptXOffset   | Adobe FDK will calculate                                            | Subscript x offset. Corresponds to the OpenType OS/2 table ySubscriptXOffset field.                                                                                                                                            |
+---------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ySubscriptYOffset   | Adobe FDK will calculate                                            | Subscript y offset. Corresponds to the OpenType OS/2 table ySubscriptYOffset field.                                                                                                                                            |
+---------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ySuperscriptXSize   | Adobe FDK will calculate                                            | Superscript horizontal font size. Corresponds to the OpenType OS/2 table ySuperscriptXSize field.                                                                                                                              |
+---------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ySuperscriptYSize   | Adobe FDK will calculate                                            | Superscript vertical font size. Corresponds to the OpenType OS/2 table ySuperscriptYSize field.                                                                                                                                |
+---------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ySuperscriptXOffset | Adobe FDK will calculate                                            | Superscript x offset. Corresponds to the OpenType OS/2 table ySuperscriptXOffset field.                                                                                                                                        |
+---------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ySuperscriptYOffset | Adobe FDK will calculate                                            | Superscript y offset. Corresponds to the OpenType OS/2 table ySuperscriptYOffset field.                                                                                                                                        |
+---------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| yStrikeoutSize      | Adobe FDK will calculate                                            | Strikeout size. Corresponds to the OpenType OS/2 table yStrikeoutSize field.                                                                                                                                                   |
+---------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| yStrikeoutPosition  | Adobe FDK will calculate                                            | Strikeout position. Corresponds to the OpenType OS/2 table yStrikeoutPosition field.                                                                                                                                           |
+---------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Panose              | Family kind: Any                                                    | The Panose classification for the font.                                                                                                                                                                                        |
+---------------------+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
