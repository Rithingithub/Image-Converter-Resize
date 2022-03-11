# Image-Converter-Resize
## TinkerHub Co-coder python project 

To create an Image converter GUI with Python, I will use the Tkinter library in Python which is the best known Python framework for building GUI application. Other than Tkinter we also need PIL library in Python which stands for Python Imaging Library.

## Team member 
1. Rithin Lehan T [https://github.com/Rithingithub/](https://github.com/Rithingithub/)
2. Fathima Thahsin [https://github.com/182003aef](https://github.com/182003aef)

## [Documentation Video](https://www.loom.com/share/1b3d1e3ed32147c7ab6a86a5a0120c22)


### tkinter
` python -m tkinter `
The tkinter package (“Tk interface”) is the standard Python interface to the Tcl/Tk GUI toolkit. Both Tk and tkinter are available on most Unix platforms, including macOS, as well as on Windows systems.

Running python -m tkinter from the command line should open a window demonstrating a simple Tk interface, letting you know that tkinter is properly installed on your system, and also showing what version of Tcl/Tk is installed, so you can read the Tcl/Tk documentation specific to that version.

Tkinter supports a range of Tcl/Tk versions, built either with or without thread support. The official Python binary release bundles Tcl/Tk 8.6 threaded. See the source code for the _tkinter module for more information about supported versions.

Tkinter is not a thin wrapper, but adds a fair amount of its own logic to make the experience more pythonic. This documentation will concentrate on these additions and changes, and refer to the official Tcl/Tk documentation for details that are unchanged.

### PIL or pillow
` pip install Pillow `

The Python Imaging Library adds image processing capabilities to your Python interpreter.

This library provides extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities.

The core image library is designed for fast access to data stored in a few basic pixel formats. It should provide a solid foundation for a general image processing tool.

### python-resize-image 1.1.20
` pip install python-resize-image `

A python package to easily resize images
This package provides function for easily resizing images.

Dependencies
Pillow 2.7++
Python 2.7/3.4
Introduction
The following functions are supported:

resize_crop crop the image with a centered rectangle of the specified size.
resize_cover resize the image to fill the specified area, crop as needed (same behavior as background-size: cover).
resize_contain resize the image so that it can fit in the specified area, keeping the ratio and without crop (same behavior as background-size: contain).
resize_height resize the image to the specified height adjusting width to keep the ratio the same.
resize_width resize the image to the specified width adjusting height to keep the ratio the same.
resize_thumbnail resize image while keeping the ratio trying its best to match the specified size.
