#
# Pygame Surface Access/Writing Example - Benchmark Program
#
# Demonstrates and compares the performance of various surface manipulation
# methods, both in Python (pysurfops.py) and C++ (via ctypes, see cppsurfops.cpp).
#
# Part of Accessing Pygame Surfaces in C++ with ctypes and Numpy Tutorial:
# http://github.com/Breakthrough/pygame-ctypes-tutorial | http://www.bcastell.com
#

import pygame
import numpy

import ctypes
import sys
import time
import os


def load_shared_lib(libname):
    # We assume the shared library is present in the same directory as this script.
    libpath = os.path.dirname(os.path.realpath(__file__))

    # Append proper extension to library path (.dll for Windows, .so for Linux)
    if sys.platform in ("win32", "cygwin"):
        libpath = os.path.join(libpath, "%s.dll" % libname)
    else:
        libpath = os.path.join(libpath, "%s.so" % libname)

    # Check that library exists (in same folder as this script).
    if not os.path.exists(libpath):
        print "Error - could not find shared library %s; could not find file:" % libname
        print " >> %s" % libpath
        return None

    return ctypes.CDLL(libpath)


def main():
    # Load our cppsurfops.cpp functions as a shared library.
    lib_cppbenchmarks = load_shared_lib("cppsurfops")
    if not lib_cppbenchmarks:
        print "Fatal error - could not load cppsurfops library! Exiting..."
        return

    print "Done."


if __name__ == "__main__":
    main()
