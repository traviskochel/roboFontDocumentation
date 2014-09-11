.. _buildingExtensions:

Building Extensions
===================

Create and build *.roboFontExt* files.

.. image:: /static/extensionBuilder.png

.. cssclass:: doctable

+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Plugin Name       | Name of the extension                                                                                                                                                              |
+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Plugin Icon       | The file can have a custom icon, if set.                                                                                                                                           |
+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Version           | Version of the extension.                                                                                                                                                          |
+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Developer         | Developer of the extension.                                                                                                                                                        |
+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Developer's URL   | Developer URL of the extension.                                                                                                                                                    |
+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| HTML help root    | Root folder where the HTML help can be found. A index.html is required.                                                                                                            |
+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Resources root    | Root folder where all the resources can be found. Resources are all necessary files except Python files.                                                                           |
+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Script Root       | Root folder where all the necessary Python files can be found.                                                                                                                     |
|                   |                                                                                                                                                                                    |
|                   | * **Launch during start up**                                                                                                                                                       |
|                   |                                                                                                                                                                                    |
|                   |   A bool indicating if a script has to be run during start up of RoboFont. Select a Python file from the list. This will be the Python file that will be executed during start up. |
|                   |                                                                                                                                                                                    |
|                   | * **Add Script to main menu**                                                                                                                                                      |
|                   |                                                                                                                                                                                    |
|                   |   Select which scripts will be added to the Extensions menu item. Additionally, a nice name and shortcut can be set for each Python file in the script root.                       |
+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Requires RoboFont | The minimum required versions of RoboFont.                                                                                                                                         |
+-------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Build
-----

Build the extension in a given folder.

Import
------

Import an existing extension.

Clear
-----

Empty all fields in the Extension Builder.

Close
-----

Close the Extension Builder window.