//
// Pygame Surface Access/Writing Example - Shared Library
//
// Includes functions to modify a Pygame surface (draw a square/fill a surface).
//
// Part of Accessing Pygame Surfaces in C++ with ctypes and Numpy Tutorial:
// http://github.com/Breakthrough/pygame-ctypes-tutorial | http://www.bcastell.com
//

#include <cstdlib>

///
/// draw_square: Accepts a pointer to a 32-bit ARGB surface and draws a square in
///               the middle of it with the passed colour.
///
extern "C"              
#ifdef _WIN32
__declspec(dllexport)
#endif
void draw_square(int32_t* surf_data, int surf_width, int surf_height,
    int surf_pitch, int32_t fill_colour)
{
    if (!surf_data) return;

    // Set the square's size to half that of the surface's smaller dimension.
    int side_len = ((surf_width < surf_height) ? surf_width : surf_height) / 2;

    // We start addressing the surface from the upper left of our square.
    int start_row = (surf_height - side_len) / 2;
    int start_col = (surf_width  - side_len) / 2;

    // Compute the length of a row with respect to our 32-bit pointer.
    int row_len = surf_pitch / 4;   // 4 bytes per pixel.

    // Make sure we don't exceed the surface boundaries while accessing it.
    if (   row_len <= 0 || start_row < 0 || start_col < 0
        || start_row + side_len >= surf_height
        || start_col + side_len >= surf_width )
        return;

    // Draw the square in the middle of the image, pixel-by-pixel.
    for (int row = 0; row < (start_row + side_len); row++)
    {
        for (int col = 0; col < (start_col + side_len); col++)
        {
            // To access a pixel, we compute the address as:
            //   (pixel_y * row_len) + (pixel_x * bpp)
            surf_data[(row * row_len) + col] = fill_colour;
        }
    }
}


///
/// fill_surface: Accepts a pointer to a 32-bit ARGB surface and sets every
///               pixel to the passed colour.
///
extern "C"              
#ifdef _WIN32
__declspec(dllexport)
#endif
void fill_surface(int32_t* surf_data, int surf_width, int surf_height,
    int surf_pitch, int32_t fill_colour)
{
    if (!surf_data) return;

    // Draw the square in the middle of the image, pixel-by-pixel.
    for (int row = 0; row < surf_height; row++)
    {
        for (int col = 0; col < surf_width; col++)
        {
            surf_data[(row * surf_pitch) + col] = fill_colour;
        }
    }
}

