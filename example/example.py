#
#
#
#

import system

def load_shared_lib(libname):

    # Append proper extension to library name (.dll for Windows, .so for Linux)
    if sys.platform in ("win32", "cli"):
        libname = "%s.dll" % libname
    else:
        libname = "lib%s.so" % libname


def main():
    print "Done."


if __name__ == "__main__":
    main()
