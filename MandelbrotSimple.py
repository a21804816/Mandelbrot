import numpy as np
from timeit import default_timer as timer
from PIL import Image
import matplotlib as mpl
import matplotlib.pyplot as plt

def mandelbrot(creal, cimag, maxiter):
    real = creal
    imag = cimag
    for n in range(maxiter):
        real2 = real*real
        imag2 = imag*imag
        imag = 2 * real*imag + cimag
        real = real2 - imag2 + creal
        if real2 + imag2 > 4.0:
            break
    return n


if __name__ == '__main__':
    xSize = ySize = 4096 
    x0 = -2.00
    y0 = -1.25
    x1 = 0.50
    y1 = 1.25
    maxIterations = 10
   
    pixelWidth = (x1-x0) / xSize
    pixelHeight = (y1-y0) / ySize

    print('Generating fractal of size {0} x {1} with {2} iterations'.format(
        xSize, ySize, maxIterations))
    print(f"Limits: x0: {x0}, y0: {y0}")
    print(f"Limits: x1: {x1}, y1: {y1}")
    print(f"Width: {x1 - x0} Height: {y1 - y0}")
    print(f"Width: {pixelWidth} Height: {pixelHeight}")

    start = timer()
    img = np.zeros((xSize, ySize), dtype=np.int32)
    for j in range(ySize):   
        cy = y0 + j*pixelHeight
        for i in range(xSize):   
            cx = x0 + i*pixelWidth
            iterations = mandelbrot(cx, cy, maxIterations)
            img[j, i] = iterations

    duration = timer() - start
    print(f'Exec time: {duration:.2f} seconds')
    plt.axis("off")
    plt.imshow(img, plt.cm.get_cmap('RdGy'))
    plt.show()