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
    |  surface.fill  |           |           |           |
    |  surface.blit  |           |           |           |
    ------------------------------------------------------
    |  *C++*:        |           |           |           |
    |  for-loop      |           |           |           |
    |  memset        |           |           |           |
    ------------------------------------------------------
    
    (tested w/ i7 2600k @ 4.0 GHz, test code can be found in `benchmarks/` directory)
    

While very useful in some cases, accessing higher-level objects can be difficult without modifying the C/C++ part of the code [into a Python module](http://docs.python.org/2/extending/extending.html#writing-extensions-in-c), or by using wrappers like [SWIG](http://www.swig.org/).  In this tutorial, we will modify a Pygame surface directly in memory using C++, without any additional dependencies/libraries.

This file (README.md) contains a brief outline of the process, which should suffice for those comfortable with ctypes and manipulating pygame/SDL surfaces directly.  A more in-depth guide can be found in TUTORIAL.md, including the creation of a demonstration application (found in the `example/` directory).


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

There are four main steps we need to complete:

 1. Write a C++ function to modify a Pygame surface in-place
 2. Compile the function into a shared library
    2.1. Compiling on Linux (gcc/g++)
    2.2. Compiling on Windows (Visual Studio)
 3. Import the shared library via Python's ctypes
 4. Access the Pygame surface as a Numpy array, obtain pointer to pixel data


### 1. Writing a C++ Function to Modify a Surface

To demonstrate writing to pixels in C++, let's create a function that draws an RGB flag onto a surface (i.e. the left third red, middle third blue, and right third green):
<img style="max-width:100%;" src="https://raw.github.com/breakthrough/pygame-ctypes-tutorial/master/images/fillrgb.png" alt="https://raw.github.com/breakthrough/pygame-ctypes-tutorial/master/images/fillrgb.png" />

For simplicity, we assume the format is 32-bit RGBA, with the red value stored in the lowest-order byte.  Note that we have to compute the address of each pixel as an offset from the start of the surface data, since we will work with a pointer directly to the pixel data (`unsigned char*`) in memory:


Since we are accessing the pixels as they sit in memory, one must ensure that the surface type is known and being [accessed correctly](http://en.wikipedia.org/wiki/Endianness).  That being said, that the above function can easily be adapted for other surface types (the [`get_masks()`](http://www.pygame.org/docs/ref/surface.html#pygame.Surface.get_pitch) and [`get_pitch()`](http://www.pygame.org/docs/ref/surface.html#pygame.Surface.get_pitch) methods are useful for correctly addressing surfaces in-memory), the same way as would be done for a regular SDL surface in C/C++.

One could technically use the SDL library functions on pygame surfaces, although this would require linking your C++ code with SDL.


----------------------------------------------------------

### 2. Compiling the C++ Function into a Shared Library

#### 2.1 Compiling on Linux (gcc/g++)

#### 2.2 Compiling on Windows (Visual Studio)


----------------------------------------------------------

### 3. Importing the Library Functions into Python via ctypes


----------------------------------------------------------

### 4. Passing a Pointer to a Surface's Pixel Data

