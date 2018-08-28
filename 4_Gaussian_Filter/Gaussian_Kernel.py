import numpy as np
from decimal import Decimal
import matplotlib.pyplot as plt

# python program to generate a gaussian kernel that is a ported from matlab's fspecial('gaussian')
# with the addition of multiplying the gaussian kernel by 1/2 * pi * sigma ^2
# taken from the stack overflow post at:
# https://stackoverflow.com/questions/17190649/how-to-obtain-a-gaussian-filter-in-python/17201686


def getGaussianKernel(shape=(6,6), sigma=0.5):

    # 2D gaussian mask - should give the same result as MATLAB's
    # fspecial('gaussian', [shape], [sigma])

    #The comments show an example shape of (6,6) with a sigma of 0.5 so the below expression expands to
    # (6 - 1) / 2
    # This is done twice
    row, column = [(ss - 1.0) / 2.0 for ss in shape]

    # x: [[-2.5 -1.5 -0.5  0.5  1.5  2.5]]
    # y: [[-2.5]
    #   [-1.5]
    #   [-0.5]
    #   [ 0.5]
    #   [ 1.5]
    #   [ 2.5]]
    #
    #   Note: x and y are of type ndarray.
    y,x = np.ogrid[-row:row + 1, -column:column + 1]

    #The below expression broken down.
    #
    # x*x = [[6.25 2.25 0.25 0.25 2.25 6.25]]
    # y*y = [[6.25]
    #        [2.25]
    #        [0.25]
    #        [0.25]
    #        [2.25]
    #        [6.25]]

    # x*x + y*y=
    # [[12.5  8.5  6.5  6.5  8.5 12.5]
    # [ 8.5  4.5  2.5  2.5  4.5  8.5]
    # [ 6.5  2.5  0.5  0.5  2.5  6.5]
    # [ 6.5  2.5  0.5  0.5  2.5  6.5]
    # [ 8.5  4.5  2.5  2.5  4.5  8.5]
    # [12.5  8.5  6.5  6.5  8.5 12.5]]

    # -(x*x + y*y) = The same as above but all negative
    # (2.0 * sigma=0.5 * sigma=0.5) = 0.5

    # -(x*x + y*y) / (2.0 * sigma * sigma) = 
    #
    # [[-25. -17. -13. -13. -17. -25.]
    # [-17.  -9.  -5.  -5.  -9. -17.]
    # [-13.  -5.  -1.  -1.  -5. -13.]
    # [-13.  -5.  -1.  -1.  -5. -13.]
    # [-17.  -9.  -5.  -5.  -9. -17.]
    # [-25. -17. -13. -13. -17. -25.]]

    #  kernel = 1 / (2 * pi * sigma * sigma) e ^ ( -(x*x + y*y) / (2.0 * sigma * sigma) ) = 
    # [[8.84133966e-12 2.63556621e-08 1.43897039e-06 1.43897039e-06 2.63556621e-08 8.84133966e-12]
    #  [2.63556621e-08 7.85651214e-05 4.28951028e-03 4.28951028e-03 7.85651214e-05 2.63556621e-08]
    #  [1.43897039e-06 4.28951028e-03 2.34199326e-01 2.34199326e-01 4.28951028e-03 1.43897039e-06]
    #  [1.43897039e-06 4.28951028e-03 2.34199326e-01 2.34199326e-01 4.28951028e-03 1.43897039e-06]
    #  [2.63556621e-08 7.85651214e-05 4.28951028e-03 4.28951028e-03 7.85651214e-05 2.63556621e-08]
    #  [8.84133966e-12 2.63556621e-08 1.43897039e-06 1.43897039e-06 2.63556621e-08 8.84133966e-12]]
    #
    kernel = (1/ (2 * np.pi * sigma * sigma) ) * np.exp( -(x*x + y*y) / (2.0 * sigma * sigma) )

    # eps -> Is the smallest representable positive number such that 1.0 + eps != 1.0
    # This seems to truncate numbers that are too small.
    kernel[ kernel < np.finfo(kernel.dtype).eps*kernel.max() ] = 0

    #Get the sum of the kernel
    kernelSum = kernel.sum()

    #Rememeber the gaussian distribution has a mean of 0
    if kernelSum != 0:
        kernel /= kernelSum

    return kernel

#uncomment to plot
#gaussian_kernel = getGaussianKernel((13,13),3)
#plt.imshow(gaussian_kernel)
#plt.colorbar()
#plt.show()
