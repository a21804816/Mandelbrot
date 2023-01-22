# Mandelbrot Set on GPU with OpenCL

This program generates an image of the Mandelbrot set using the OpenCL framework for GPU computation. It demonstrates how to use the PyOpenCL library to write a parallelized program that generates the fractal image on the GPU.

<img width="640" alt="mandelbrot" src="https://user-images.githubusercontent.com/43844931/213940275-7d2410e7-a59c-4ad6-9cb4-615e483e3f95.png">


# Requirements

PyOpenCL

Numpy

Matplotlib

# Usage

To run this program, you'll need to have PyOpenCL, numpy, and matplotlib installed on your system. Then, you can run the script from the command line by calling python mandelbrot_gpu.py.

The program starts by creating an OpenCL context and command queue. Then, it allocates memory on the GPU for the output image and creates an OpenCL kernel that will be executed on the GPU.

The kernel is responsible for generating the Mandelbrot set. It takes four parameters: the output image buffer, the width and height of the image, and the maximum number of iterations. The kernel uses the global ID of the current thread to determine the coordinates of the pixel being computed. The value of the pixel is computed by iterating the Mandelbrot equation and counting the number of iterations before the value exceeds 4. The final value is stored in the output image.

The kernel is then executed on the GPU with the global_size and local_size parameters specifying the number of threads to use. The program also measure the time of execution to show the performance of the computation.

Finally, the image is copied back from the GPU to the CPU and displayed using matplotlib. The imshow() function is used to display the image and the RdGy colormap is used to color the image.

# Notes

The size of the image can be modified by changing the width and height variables.

The maximum number of iterations can be modified by changing the maxIt variable.

# Results

| Method | Image Size | Max Iterations | Execution Time (seconds) |
| :---         |     :---:      |          :---: | :---: |
| Mandelbrot CPU   | 4096 x 4096   | 100   |  88.57   |
| Mandelbrot GPU   | 4096 x 4096   | 100     |  0.58   |

# Hardware 

Macbook Pro M1 8GB

MacOs Ventura 13.1

