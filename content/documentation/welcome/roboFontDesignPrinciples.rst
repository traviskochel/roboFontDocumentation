.. _roboFontDesignPrinciples:

RoboFont design principles
==========================

Motivation
----------

A typeface designer (who does not want to do any scripting and has no means of letting someone else do that work), has to deal with the available user interface, tool set, feature set, and the list of bugs in the typeface design applications they use. This makes the designer a victim to the development of applications that are often merely production tools and not intended for design iterations. Not being (partly) the designer of your own tools puts a designer in a vulnerable position.

Specialized tools
-----------------

Spreading functions over different tools reduces the need to buy them all at the same time, or pay for the development of a function you don’t require. Or you can do better yourself and write your own custom tool for a function. Functions can be added over time as they become available and technology changes.

Decentralized development also means that a group of people can work on the functions that they really do need and are extremely capable of making and maintaining.

The role of RoboFont
--------------------

The idea behind RoboFont is to provide a sturdy framework where everyone can add their own functionalities with Python, rather than a program with hundreds of (often little needed) functions.

Constructing an open structure for RoboFont allows any developer to add new technologies to the overall functionality, without the need for the main developer(s) to put it on top of their list. It also allows competition between ideas and technologies, as any developer’s idea of how something should work can be part of RoboFont.

This is very different from having one application that can only do most of the things on a average level. It also means that upgrading a single function implies upgrading the entire application, which often is not attractive to a developer. This can result in a lag between the introduction of a new technology/upgraded function and the ability to use that technology/upgraded function. Lastly, one is locked into the developer’s idea of how a function should work, rather than being able to choose how the function should work for you.

No previous knowledge
---------------------

An application shouldn’t design for a designer, as it is just a tool. Pencils do not illustrate, printing presses do not layout, and a typeface design application shouldn’t make autonomous decisions. The typeface designer should make the decisions and have the power to design their fonts.

Think of RoboFont as a second desktop for your typeface design work. Like your physical desk, it can be customized for different kinds of design work. For example, your settings can be very different if you are designing a headline typeface or working on a revival. RoboFont allows you to change and optimize your editor settings from project to project.

Full scripting support
----------------------

RoboFont is programmed in Python from the ground up. The entire application is object oriented, allowing any user to dive into the deep functionality of RoboFont and overwrite/redefine/add functions —even at the core of the program— simply by inheriting the existing classes. This way there is a total melding between scripting and coding of the main application.

A platform for building custom tools and extensions
---------------------------------------------------

RoboFont is a rich environment for developing one’s own custom tools. The extensibility of it’s object model allows a designer to build whatever they can think of on the base of RoboFont. If a designer isn’t inclined to write additional tools for the RoboFont environment, one can see a near-term future for the sharing or sale of scripts and extension to RoboFont.