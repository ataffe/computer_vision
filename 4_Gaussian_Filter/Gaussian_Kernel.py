import numpy as np

def getGaussianKernel(shape=(6,6), sigma=0.5):

    # 2D gaussian mask - should give the same result as MATLAB's
    # fspecial('gaussian', [shape], [sigma])

    #shape is a tuple of (6,6) so the below expression expands to
    # (6 - 1) / 2
    # This is done twice
    m, n = [(ss - 1.0) / 2.0 for ss in shape]

    # x: [[-2.5 -1.5 -0.5  0.5  1.5  2.5]]
    # y: [[-2.5]
    #   [-1.5]
    #   [-0.5]
    #   [ 0.5]
    #   [ 1.5]
    #   [ 2.5]]
    #
    #   Note: x and y are of type ndarray.
    y,x = np.ogrid[-m:m + 1, -n:n + 1]

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

    #  h = e ^ ( -(x*x + y*y) / (2.0 * sigma * sigma) ) = 
    # [[1.38879439e-11 4.13993772e-08 2.26032941e-06 2.26032941e-06 4.13993772e-08 1.38879439e-11]
    # [ 4.13993772e-08 1.23409804e-04 6.73794700e-03 6.73794700e-03 1.23409804e-04 4.13993772e-08]
    # [ 2.26032941e-06 6.73794700e-03 3.67879441e-01 3.67879441e-01 6.73794700e-03 2.26032941e-06]
    # [ 2.26032941e-06 6.73794700e-03 3.67879441e-01 3.67879441e-01 6.73794700e-03 2.26032941e-06]
    # [ 4.13993772e-08 1.23409804e-04 6.73794700e-03 6.73794700e-03 1.23409804e-04 4.13993772e-08]
    # [ 1.38879439e-11 4.13993772e-08 2.26032941e-06 2.26032941e-06 4.13993772e-08 1.38879439e-11]]
    #
    # h is a 6 x 6 matrix
    h = np.exp( -(x*x + y*y) / (2.0 * sigma * sigma) )
    
    #Note: find out what eps is.
    # esp -> Is the smallest representable positive number such that 1.0 + eps != 1.0
    if(h < np.finfo(h.dtype).eps*h.max()):
        print("h < np.finfo(h.dtype).eps*h.max(): " + str(h < np.finfo(h.dtype).eps*h.max()) )
        
    h[ h < np.finfo(h.dtype).eps*h.max() ] = 0

    print(np.finfo(h.dtype))

    #Get the sum of the kernel
    sumh = h.sum()

    #Rememeber the gaussian distribution has a mean of 0
    if sumh != 0:
        h /= sumh

    return h




getGaussianKernel()


#Example from stack overlfow.

def matlab_style_gauss2D(shape=(3,3),sigma=0.5):
    """
    2D gaussian mask - should give the same result as MATLAB's
    fspecial('gaussian',[shape],[sigma])
    """
    m,n = [(ss-1.)/2. for ss in shape]
    y,x = np.ogrid[-m:m+1,-n:n+1]
    h = np.exp( -(x*x + y*y) / (2.*sigma*sigma) )
    h[ h < np.finfo(h.dtype).eps*h.max() ] = 0
    sumh = h.sum()
    if sumh != 0:
        h /= sumh
    return h