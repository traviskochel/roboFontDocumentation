.. _api:

API
===

RoboFont is highly extendable in any direction from subclassing existing classes to adding new features and functionality in a new tool.

There are many levels how to interact with RoboFont and how to handle various parts: font data, UI, user interaction, ...

Scripts
-------

A tiny script using `roboFab <http://doc.robofont.com/api/robofab-extras/>`_ to add actions/features/functionalities to a menu item or key stroke.

.. showcode:: /RoboFontExamples/fonts/monoMaker.py

Save this script in the default script folder to extend RoboFont Extensions menu. See the :ref:`preferences` to add a short cut to a specific script.

Observers & Tools
-----------------

RoboFont is being build up around a core that is just sending out notifications. A script can subscribe to one or more notifications and perform an action based on the send notification.

There are three kinds of notifications inside RoboFont:

*   `Native Cocoa Notifications <https://developer.apple.com/library/mac/documentation/Cocoa/Conceptual/Notifications/Articles/NotificationCenters.html>`_

    When the app opens, closes, hides; when a window resizes; when a text field changed, ...

*   `Font Data Notifications <https://github.com/typesupply/defcon>`_

    Font data notifications are being send out when the font data is being changed. Those notifications are already natively in `defcon <https://github.com/typesupply/defcon>`_ and extended in RoboFont.

*   :ref:`RoboFont Notifications <apiObservers>`

    RoboFont notifications are being send from several places: Glyph Editor, Space Centers, based on users interaction related to adjusting, changing font data.

There are two systems build in to subscribe to notifications:

*   :ref:`As an Observer <apiObservers>`

    A class, the observer will subscribe to a specific notification. When the notification is being send it will receive a callback with additional info and objects related to the notification.

*   :ref:`As a Tool <apiTools>`

    A tools receives all the notifications RoboFont has, but it only can be activated when an user selected the tool from the toolbar in the glyph editor.

.. toctree::
    :maxdepth: 2
    :titlesonly:
    :hidden:

    API/scriptingGuidelines
    API/observers
    API/tools
    API/embeddedPackages
    API/robofabExtras
    API/mojo
    API/genindexRedirect


