.. _mojo.extensions:

mojo.extensions
===============

::

    from mojo.extensions import *

.. class:: ExtensionBundle(name=None, path=None, libName="lib", htmlName="html", indexHTMLName="index.html", resourcesName="Resources")

    An extension bundle objects allowing access to different parts of an extension.

    initiate an ExtensionBundle object

    .. describe:: name

        name of an extension (either name or path is required)

    .. describe:: path

        path to an extension (either name or path is required)

    .. function:: getExtensionDefault(key, fallback=None)

        returns the value for key from the extension user defaults
        if the key isn't used it returns the fallback

    .. function:: setExtensionDefault(key, value)

        set the value for key in the extensions user defaults

    .. function:: getExtensionDefaultColor(key, fallback=None)

        returns an NSColor object for key from the extension user defaults

    .. function:: setExtensionDefaultColor(key, fallback=None)

        set an NSColor for key in the extensions user defaults

    .. function:: registerExtensionsDefaults(defaults)

        register a dict with keys and values as defaults in the extension user defaults

    .. function:: get(name, ext='\*')

        returns the file within the extension, if its is an image it will return the NSImage object around that image.

    .. function:: install()

        installs the extension

    .. function:: deinstall()

        de-installs the extension

    .. function:: openHelp()

        Opens the help HTML in an HTMLHelpWindow

    .. function:: validate()

        validates the extension

    .. function:: validateErrors()

        returns a string of validation errors

    .. function:: bundlePath()

        returns the path of the extension bundle

    .. function:: libPath()

        returns the path of the lib folder inside the bundle

    .. function:: HTMLPath()

        returns the path of the HTML folder inside the bundle

    .. function:: resourcesPath()

        returns the path of the Resources folder inside the bundle

    .. function:: infoDictionaryPath()

        returns the path of the info.plist inside the bundle

    .. function:: mainScriptPath()

        returns the path of the main script

    .. function:: hasHTML()

        returns a bool if the extension has HTML help

    .. function:: HTMLIndexPath()

        returns the path of the index.html file

    .. function:: bundleExists()

        returns if a bool if the extension bundle exists on disk

    .. function:: allExtensions()

        a class method returns all installed extensions

    .. attribute:: version

        returns the version of the extension

    .. attribute:: name

        returns the name of the extension

    .. attribute:: developer

        returns the developer of the extension

    .. attribute:: developerURL

        returns the developer URL of the extension

    .. attribute:: requiresVersionMajor

        returns the required major version number of RoboFont

    .. attribute:: requiresVersionMinor

        returns the required minor version number of RoboFont

    .. attribute:: addToMenu

        returns a bool if the bundle should be added to the extension menu

    .. attribute:: launchAtStartUp

        returns a bool if the bundle should be launched at start up

    .. attribute:: mainScript

        returns the filename of the main script

    .. attribute:: timeStamp

        returns the time stamp, stamped when the extension is build

