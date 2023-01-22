import numpy as np
import pyopencl as cl
import matplotlib.pyplot as plt
from timeit import default_timer as timer

width = 4096  
height = 4096   
maxIt = 100

# Create OpenCL context and command queue
ctx = cl.create_some_context()
queue = cl.CommandQueue(ctx)

# Allocate memory for the output image on the GPU
image = np.empty((width, height), dtype=np.uint8)
image_buf = cl.Buffer(ctx, cl.mem_flags.WRITE_ONLY, image.nbytes)

# Create and build OpenCL kernel
kernel = """
__kernel void mandelbrot(__global uchar *image, int width, int height, int maxIt) {
    int gid_x = get_global_id(0);
    int gid_y = get_global_id(1);

    float x = (gid_x / (float)width) * 3.5 - 2.5;
    float y = (gid_y / (float)height) * 2.0 - 1.0;

    float real = x;
    float imag = y;

    int value = 0;
    int i = 0;
    while (i < maxIt && value < 4) {
        float r2 = real * real;
        float i2 = imag * imag;

        imag = 2 * real * imag + y;
        real = r2 - i2 + x;

        value = r2 + i2;
        i++;
    }

    image[gid_y * width + gid_x] = i;
}
"""
start = timer()
prg = cl.Program(ctx, kernel).build()

global_size = (width, height)
local_size = None

# Execute kernel on the GPU
prg.mandelbrot(queue, global_size, local_size, image_buf, np.int32(width), np.int32(height),np.int32(maxIt))

# Copy the result from GPU to CPU
cl.enqueue_copy(queue, image, image_buf)

duration = timer() - start

# Plot the image

print(f'Generating fractal of size {width}x{height} with {maxIt} iterations')
print(f'Total processing time: {duration:.2f} seconds')  
plt.axis("off") 
plt.imshow(image, cmap='RdGy')
plt.show()