.. _scripting:

Scripting
=========

A python editor to write and execute python files inside RoboFont. There are lots of embedded packages and tools to write code and extent RoboFont lots of possible features.

The code text editor is build for writing python code. Syntax highlights python specific tokens.

You can browse your predefined scripting folder. Double click will set the selected file in the code editor.

.. image:: /static/scriptingWindow.png

.. cssclass:: doctable

+--------------+------------------------------------------------+
| Run          | run the current script                         |
+--------------+------------------------------------------------+
| Comment      | comment the selected line(s)                   |
+--------------+------------------------------------------------+
| Uncomment    | uncomment the selected line(s)                 |
+--------------+------------------------------------------------+
| Indent       | indent the selected line(s)                    |
+--------------+------------------------------------------------+
| Dedent       | decent the selected line(s)                    |
+--------------+------------------------------------------------+
| Save         | save the file as a \*.py file                  |
+--------------+------------------------------------------------+
| Reload       | reload the file from disk                      |
+--------------+------------------------------------------------+
| New          | create a new python document                   |
+--------------+------------------------------------------------+
| Open         | open a \*.py file                              |
+--------------+------------------------------------------------+
| Edit With... | edit the file with the preferred python editor |
+--------------+------------------------------------------------+

.. _outputWindow:

Output Window
-------------

This window catches all print statements and tracebacks when a script is not running in the scripting window.

Enable "Can hide" to hide the window when RoboFont is not the active app anymore. (It acts like a floating window). When disabled the window will still be visible when RoboFont is not active.

*Clear* will empty the all print statements and traceback from the Output window.

.. image:: /static/outputWindow.png

Command Line
------------

RoboFont is accessible through command line. Install the command line tool in the :ref:`preferences`.

The command line tool is using a very simple API:

::

    Call RoboFont to execute python files:
    roboFont [-h] [-p] [-c] [-o]
    --help -h                               options
    --pythonpath -p <path> <path> ...      .py files path(s) to run inside RoboFont
    --pythoncode -c "print 5*5"             python code to run inside RoboFont
    --openfile -o <path>                    files to open with RoboFont

|

.. raw:: html

    <iframe src="http://player.vimeo.com/video/42008861" width="100%" height="431" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>


Read more: :ref:`API`, :ref:`preferences`
