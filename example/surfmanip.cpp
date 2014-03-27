//
// Pygame Surface Access/Writing Example 
//
// Part of Accessing Pygame Surfaces in C++ with ctypes and Numpy Tutorial:
// http://github.com/Breakthrough/pygame-ctypes-tutorial | http://www.bcastell.com
//

///
/// fill_surface: Accepts a pointer to a 32-bit ARGB surface and draws a square in
///               the middle of it with the passed colour.
///
extern "C"              
#ifdef _WIN32
__declspec(dllexport)
#endif
void fill_surface(unsigned char* surf_data, int surf_width, int surf_height,
    int surf_stride, unsigned char rval, unsigned char gval, unsigned char bval)
{
    unsigned char* pixel_ptr;   // Used to access the surface below.

    // Set the square's size to half that of the surface's smaller dimension.
    int side_len = ((surf_width < surf_height) ? surf_width : surf_height) / 2;

    // We start addressing the surface from the upper left of our square.
    int start_row = (surf_height - side_len) / 2;
    int start_col = (surf_width  - side_len) / 2;

    // Make sure we don't exceed the surface boundaries while accessing it.
    if (   start_row < 0 || start_col < 0
        || start_row + side_len >= surf_height
        || start_col + side_len >= surf_width )
        return;

    // Draw the square in the middle of the image, pixel-by-pixel.
    for (int row = 0; row < (start_row + side_len); row++)
    {
        for (int col = 0; col < (start_col + side_len); col++)
        {
            // To access a pixel, we compute the address as:
            //   (pixel_y * stride) + (pixel_x * bpp)
            // Where stride is the length of 1 row of the image (in bytes) in
            // memory, and bpp is the size of a pixel (in bytes).
            pixel_ptr = surf_data + (row * surf_stride) + (col * 4);
            // In ARGB format, the pixel values are packed together, so we can
            // just access each sequential byte as the next color;
            // pixel_ptr[0] = 0xFF; // We don't touch the alpha value.
            pixel_ptr[1] = rval;    // Red value.
            pixel_ptr[2] = gval;    // Green value.
            pixel_ptr[3] = bval;    // Blue vlaue.
        }
    }
}
