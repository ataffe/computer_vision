# Gaussian Filter

This is the folder for the gaussian filter quiz on teh udacity course ud810. I used the opencv functions:  

[kernel = getGaussianKernel(hsize, sigma)](https://docs.opencv.org/3.0-beta/modules/imgproc/doc/filtering.html#getgaussiankernel)  

where  

**hsize** = the kernel size.  
**sigma** = the gaussian distribution sigma.  

To create a gaussian kernel with an input hsize and sigma and the function:  

[image = filter2D(image, -1, kernel)](https://docs.opencv.org/2.4/modules/imgproc/doc/filtering.html#filter2d)

where   

**image** = the image that will blurred or convolved with the input kernel.  
**kernel** = the kernel that the image will be convolved with.  

To apply the kernel to the image.

# Blurred Image
![alt text](https://raw.github.com/ataffe/computer_vision/master/Gaussian_Filter/PeoriaCityHall_blur.jpg)

# Noise Image
![alt text](https://raw.github.com/ataffe/computer_vision/master/Gaussian_Filter/PeoriaCityHall_noisy.jpg)

# Original Image
![alt text](https://raw.github.com/ataffe/computer_vision/master/Gaussian_Filter/PeoriaCityHall.JPG)


