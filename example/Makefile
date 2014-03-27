#
# Pygame Surface Access/Writing Example 
#
# Part of Accessing Pygame Surfaces in C++ with ctypes and Numpy Tutorial:
# http://github.com/Breakthrough/pygame-ctypes-tutorial | http://www.bcastell.com
#

all: surfmanip.so

# -Wl passes options to linker, -fPIC to emit position-independent code
surfmanip.so: surfmanip.cpp
	g++ -Wall -shared -O3 -Wl,-soname,surfmanip.so -o surfmanip.so -fPIC surfmanip.cpp

clean:
	rm -f surfmanip.so
