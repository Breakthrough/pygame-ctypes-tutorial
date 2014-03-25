#
#
#
#

import pygame

import system
import time

WINDOW_RESOLUTION = (720, 480)
SHARED_LIB_NAME   = "surfmanip"


def load_shared_lib(libname):

    # Append proper extension to library name (.dll for Windows, .so for Linux)
    if sys.platform in ("win32", "cli"):
        libname = "%s.dll" % libname
    else:
        libname = "lib%s.so" % libname



def main():


    screen = pygame.display.set_mode(WINDOW_RESOLUTION)

    cpp_shared_lib = load_shared_lib(SHARED_LIB_NAME)

    if not cpp_shared_lib:
        print "Fatal error - could not load shared library %s." % SHARED_LIB_NAME
        return


    # Call our C++ function to modify the screen surface pixels directly.
    #cpp_shared_lib.modify_surf(ctypes.) ...
        

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

        time.sleep(0.1)


    print "Done."


if __name__ == "__main__":
    main()
