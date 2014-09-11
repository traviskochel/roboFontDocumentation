.. _features:

Features
========

.. image:: /static/toolbarFeatures.png

Write your Open Type features using the `Adobe feature syntax <http://www.adobe.com/devnet/opentype/afdko/topic_feature_file_syntax.html>`_ in the `UFO <http://unifiedfontobject.org>`_ file. See also `Tal Leming <https://typesupply.com/>`_'s `Open Type Cookbook <http://opentypecookbook.com/>`_.

Note: If you are using :ref:`kernCenter` or `MetricsMachine <http://tools.typesupply.com/metricsmachine.html>`_, your kerning is added automatically to the features, you should not define a kerning feature here. If you have defined a kern feature in the feature file, then this will be used instead of the kerning set in the UFO file.

A feature editor accepts drag and drop of *.fea* files. The dropped files will be inserted as *include(path/of/the/dropped/feature/file.fea)*.

External Feature Editor
-----------------------

RoboFont support *.fea* as a file format. Double click a *.fea* file will open the feature file in a separate feature editor which is not connected to a UFO.

.. image:: /static/externalfeatureSupport.png

New Feature
^^^^^^^^^^^

Create a new feature document. This is feature document is not connected to a UFO file. It will be saved as *.fea* file.

.. image:: /static/featureEditor.png

.. cssclass:: doctable

+-----------------+---------------------------------------------------------------+
| Insert In Fonts | Pop up a sheet to add the feature text to the selected fonts. |
+-----------------+---------------------------------------------------------------+
| Save            | Save the feature file.                                        |
+-----------------+---------------------------------------------------------------+
| Reload          | Reload the feature file from disk.                            |
+-----------------+---------------------------------------------------------------+

Export Feature
^^^^^^^^^^^^^^

Export the features from the current font to a *.fea* file.