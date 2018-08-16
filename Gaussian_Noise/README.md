# Gaussian Noise

This folder is for the gaussian noise quize on the udacity course. I created a function in python to add random normal noise to an image using the function:

[numpy.random.normal()](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.normal.html)
Then added it to the image like so:  

noisyImage = Image + (numpy.random.normal(mean,sigma,(rows,columns)))

where:

**Image** = the image to add noise to.  
**mean** = The mean of the gaussian distribution.  
**sigma** = The standard distribution of the gaussian distribution.
**rows** = The number of rows for the matrix of random numbers that will be generated. (Should match the number of rows in the image.)  
**columns** = The number of columns for the matrix of random numbers that will be generated. (Should match the number columns in the image.)  

Side Note: It kind of makes the image look, old timey like it was taken with a black n white camera a long time ago. I wonder if images with those cameras had a lot of noise?
![alt text](https://raw.github.com/ataffe/computer_vision/master/Gaussian_Noise/noisy.jpg)
