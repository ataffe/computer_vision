# Gaussian Filter
note: This module is built for python 3 becuase it uses tkinter to adjust both sigmas and kernel size. See the computer_vision folder for how to install python 3, opencv 3, matplotlib, and numpy. 



This is the folder for the gaussian filter quiz on the udacity course ud810. I used the opencv functions:  
(This is wrong it doesn't return a circular symmetric gaussian distribution)  
[kernel = getGaussianKernel(hsize, sigma)](https://docs.opencv.org/3.0-beta/modules/imgproc/doc/filtering.html#getgaussiankernel)  

where  

**hsize** = the kernel size.  
**sigma** = the gaussian distribution sigma.  

The kernel is generated based on a circular symmetric gaussian distribution(atleast I hope it is):

![alt text](https://raw.github.com/ataffe/computer_vision/master/Math_Screenshots/circular_sym_gauss.PNG)

To apply the kernel to the image I used the function:

[image = filter2D(image, -1, kernel)](https://docs.opencv.org/2.4/modules/imgproc/doc/filtering.html#filter2d)

where   

**image** = the image that will blurred or convolved with the input kernel.  
**kernel** = the kernel that the image will be convolved with.  

To apply the kernel to the image.

# Blurred Image
(Kernel Size = 1023   Sigma = 5)
![alt text](https://raw.github.com/ataffe/computer_vision/master/1_Gaussian_Filter/PeoriaCityHall_blur.jpg)

# Noise Image
(Sigma = 32)
![alt text](https://raw.github.com/ataffe/computer_vision/master/1_Gaussian_Filter/PeoriaCityHall_noisy.jpg)

# Original Image
![alt text](https://raw.github.com/ataffe/computer_vision/master/1_Gaussian_Filter/PeoriaCityHall.JPG)


