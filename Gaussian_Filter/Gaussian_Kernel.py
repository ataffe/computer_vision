import numpy

def getGaussianKernel(shape=(6,6), sigma=0.5):

    # 2D gaussian mask - should give the same result as MATLAB's
    # fspecial('gaussian', [shape], [sigma])

    m, n = [(ss - 1.0) / 2.0 for ss in shape]
    y,x = np.ogrid[-m:m + 1, -n:n + 1]
    print("m: " + str(m))
    print("n: " + str(n))



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