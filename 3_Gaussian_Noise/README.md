# Gaussian Noise

This folder is for the gaussian noise quize on the udacity course. I created a function in python to add random normal noise to an image using the function:

[numpy.random.normal()](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.normal.html)

which generates random numbers using the probability density function:
![alt text](https://raw.github.com/ataffe/computer_vision/master/Math_Screenshots/Gaussian_Noise.PNG)  

The python function generates a matrix of random numbers of size "rows" x "colmuns". Then I added it to the image like so:  
``` python
noisyImage = Image + (numpy.random.normal(mean,sigma,(rows,columns)))
```
where:

**Image** = the image to add noise to.  
**mean** = The mean of the gaussian distribution.  
**sigma** = The standard distribution of the gaussian distribution.  
**rows** = The number of rows for the matrix of random numbers that will be generated. (Should match the number of rows in the image.)  
**columns** = The number of columns for the matrix of random numbers that will be generated. (Should match the number columns in the image.)  

Note: The matrix size must be the same size as the image, because...linear algebra. See below for an example.

# Noisy Image
Side Note: I scaled the image but I didn't mean to zoom in, it looks like the image in zoomed in on the clock

Side Side Note: It kind of makes the image look, old timey like it was taken with a black n white camera a long time ago. I wonder if images with those cameras had a lot of noise?
![alt text](https://raw.github.com/ataffe/computer_vision/master/Gaussian_Noise/noisy.jpg)

# Original Image
![alt text](https://raw.github.com/ataffe/computer_vision/master/Gaussian_Noise/grand.jpg)

# Adding two matrices
The following example is from: https://www.varsitytutors.com/hotmath/hotmath_help/topics/adding-and-subtracting-matrices

This is why the noise matrix must be the same size as the image.
![alt text](https://raw.github.com/ataffe/computer_vision/master/Math_Screenshots/adding_matrices.PNG) 
