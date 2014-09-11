.. _addingAndDeletingGlyphs:

Adding And Deleting Glyphs
==========================

Adding Glyphs
-------------

An Add glyphs sheet will shown the place to append glyphs to a font

*Application menu ⇢ Font ⇢ Add Glyphs*

.. image:: /static/addingGlyphs.png

In the text editor users can type glyph names to add the font. It should be a space sperated list of glyph names

Glyph name formatting
---------------------

*   **<glyphName>**

    *a agrave*

    Creates a glyph with the given glyph name.

*   **<glyphName>=<baseGlyphName>+<baseGlyphName>…**

    *agrave=a+grave*

    Creates a glyph with the given glyph name and adds a component referenced to glyph named 'a' and 'grave' to a glyph named 'agrave'.

    (There are no spaces in the simple glyph math)

*   **<glyphName>=<baseGlyphName>+<baseGlyphName>@<anchorName> …**

    *agrave=a+grave@top*

    Creates a glyph with the given glyph name and adds a component referenced to a glyph named 'a' and 'grave' to a glyph named 'agrave'

    The position 'top' is a reference to an anchor to specify the offset. Both glyph must have an anchor with <anchorName> and <_anchorName>.

*   **<glyphName>|<unicode>**

    *a|0061*

    Creates a glyph with the givin glyph name and adds unicode value '0061' to glyph named 'a'.

*   **<glyphName>=<baseGlyphName>+<baseGlyphName>…|<unicode>**

    *agrave=a+grave|00E0*

    Combine all glyph name formating. Creates a glyph with the givin glyph name and adds a components referenced to glyph named 'a' and 'grave' to a glyph named 'agrave' and adds unicode value '00E0' to glyph named 'agrave'

    (There are no spaces in the simple glyph math)


Enable Add Unicode to generate unicodes for the newly created glyphs. Enable Sort Font to resort the font after glyphs has been added.


Deleting Glyphs
---------------

Select a glyph or range of glyphs (shift or option click) in the Font Collection. Press del or backspace to remove glyphs from the font. A warning will be shown because this action is not undoable. To remove both the glyph and template glyph alt + del or alt + backspace.

Read more: :ref:`applicationMenu`

