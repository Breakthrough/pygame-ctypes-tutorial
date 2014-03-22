Accessing Pygame Surfaces in C++ with ctypes and Numpy
==========================================================
By: [Brandon Castellano](http://www.bcastell.com)

----------------------------------------------------------

With ctypes, you can mix C/C++ code with Python to gain the speed of compiled code with the awesomeness of Python.  How much speed are we talking about?  When compiled with optimizations enabled, the compiled functions provide a significant performance gain - sometimes exceeds even native Pygame methods, such as filling a surface:

    ------------------------------------------------------
    |  Surface Fill  |      Time to Fill Surface (ms)    |
    |     Method     |  1280x720 | 1920x1080 | 2560x1600 |
    ------------------------------------------------------
    |  *Python*:     |           |           |           |
    |  surfarray[:]  |           |           |           |
    |  surface.fill   |           |           |           |
    |  surface.blit  |           |           |           |
    ------------------------------------------------------
    |  *C++*:        |           |           |           |
    |  for-loop      |           |           |           |
    |  memset        |           |           |           |
    ------------------------------------------------------
    
    (tested w/ i7 2600k @ 4.0 GHz, test code can be found in `benchmarks/` directory)
    

While very useful in some cases, accessing higher-level objects can be difficult without modifying the C/C++ part of the code [into a Python module](http://docs.python.org/2/extending/extending.html#writing-extensions-in-c), or by using wrappers like [SWIG](http://www.swig.org/).  In this tutorial, we will modify a Pygame surface directly in memory using C++, without any additional dependencies/libraries.  This file (README.md) contains a brief outline of the process; those less familiar with pygame or ctypes may want to read TUTORIAL.md for an in-depth guide, which is related to the sample code in the `example/` directory.


Requirements
------------
 - Python (should work on both 2 and 3, tested on 2)
 - pygame (> 1.8) and Numpy
 - a C++ compiler (tested w/ g++ on Linux and VS2010 on Windows)
 - that's it!

File List
---------

 - `README.md` : Quickstart covering process for accessing Pygame surface data with C++ code.
 - `TUTORIAL.md` : Step-by-step tutorial of the process, including a sample Pygame program.
 - `example/` : Sample Python/C++ code for this tutorial; includes a Makefile for *NIX people that have `g++` and a Visual Studio project for Windows users.
 - `benchmarks/` : Python program and C++ shared library comparing the performance of various surface access methods/operations in both languages.
  
 
----------------------------------------------------------

Quickstart
----------

Coming soon!  Outline of this section:

 - Write C++ Function to Modify Surface Data Directly Through Pointer
 - Create Pygame surface and Access as Numpy Array through `surfarray`
 - Import Shared Library via ctypes
 - Display Updated Surface to Screen (or do other work w/ surface)
 
