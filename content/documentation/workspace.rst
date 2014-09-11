.. _workspace:

Workspace
=========

.. toctree::
    :maxdepth: 2
    :titlesonly:
    :hidden:

    workspace/fontCollection
    workspace/glyphEditor
    workspace/metrics
    workspace/fontInfo
    workspace/features
    workspace/groupEditor
    workspace/inspector
    workspace/scripting
    workspace/preferences
    workspace/applicationMenu

RoboFont contains lots of different windows and views, each one connected to a specific function.

Editor environment
------------------

Different application windows can be displayed separately or collected into a single window.

Read more: :ref:`preferences`

.. image:: /static/windowMode.png

Single Window mode
------------------

.. image:: /static/singleWindowMode.png

Multi Window mode
------------------

.. image:: /static/multiWindowMode.png

Font Collection
---------------

.. image:: /static/fontCollection.png

Displays all glyphs in the font, allows sorting with groups, filters, smart lists, etc.

Read more: :ref:`fontCollection`

Glyph Editor
------------

.. image:: /static/glyphEditor.png

Displays one single glyph for editing.

Read more: :ref:`glyphEditor`


Metrics
-------

.. image:: /static/spaceCenterWindow.png

Both Space Center and Kern Center display a string of glyphs for testing words and working on spacing and kerning.

Read more: :ref:`spaceCenter`, :ref:`kernCenter`

Scripting Editor
----------------

.. image:: /static/scriptingWindow.png

The scripting editor is the place to write and run Python scripts.

Read more: :ref:`scripting`

Extensions
----------

.. image:: /static/extensionWindow.png

RoboFont can easily be extended with additional features and add-ons. Developers can use the Extensions Builder to package RoboFont plugins.

Read more: :ref:`extensions`

Preferences
-----------

.. image:: /static/preferencesWindow.png

RoboFont allows users to customize many aspects of its interface and behavior through the Preferences window.

Read more: :ref:`preferences`

Additional Sheets and assisting Windows
---------------------------------------

All sheets and assisting windows will apply the changes with enter down and close with *esc* or *command+.* down. If a *close* or *OK* / *Apply* button is provided.

* **Jump to glyph**

  Accessible in the Glyph Editor and Space Center with a hot key (set in the Preferences)

* **Jump to line**

  Accessible in the Scripting code editor and Feature editor with 'command+j'










