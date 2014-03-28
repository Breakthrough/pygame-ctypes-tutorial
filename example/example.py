#
# Pygame Surface Access/Writing Example - Demonstration Program
#
# Demonstrates creating a Pygame window, and modifying the underlying surface
# directly with the shared library functions compiled in surfmanip.so/surfmanip.dll.
# Note that this may need to be modified for non 32-bit ARGB surfaces.
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

    screen = pygame.display.set_mode((720, 480))

    lib_surfmanip = load_shared_lib("surfmanip")
    if not lib_surfmanip:
        print "Fatal error - could not load surfmanip library! Exiting..."
        return

    # Get a handle to the draw_square(...) function in our shared library.
    draw_func = lib_surfmanip.draw_square
    draw_func.restype = None     # Set return type (None for void, defaults to ctypes.c_int).
    # Arguments: surf. data ptr, width, height, stride, red val, blue val, green val
    draw_func.argtypes = [ numpy.ctypeslib.ndpointer(ctypes.c_int32),
                           ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int32 ]

    # Call our C++ function to draw a red (0xFF0000) box onto the screen pixels.
    draw_func( pygame.surfarray.pixels2d(screen), screen.get_width(),
               screen.get_height(), screen.get_pitch(), 0xFF0000 )

    run_main_loop = True
    while run_main_loop:
        # Flip the screen so the window is drawn/updated.
        pygame.display.flip()
        # Handle keyboard input (quit on escape or Q).
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESC:
                    run_main_loop = False
        time.sleep(0.1)   # Idle for a bit so we don't consume 100% CPU.

    print "Done."


if __name__ == "__main__":
    main()
