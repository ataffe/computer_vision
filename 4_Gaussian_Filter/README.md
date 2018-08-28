# Gaussian Filter
##### Note: This module is built for python 3 becuase it uses tkinter to adjust both sigmas and kernel size. See the computer_vision folder for how to install python 3, opencv 3, matplotlib, and numpy. 
--- 

This is the folder for the gaussian filter quiz on the udacity course ud810. With the help of stack overflow, I created a function based on the matlab function fspecial('gaussian', [shape], [sigma]) that creates a gaussian kernel using the formula for a 2D gaussian function:  

![alt text](https://raw.github.com/ataffe/computer_vision/master/Math_Screenshots/circular_sym_gauss.PNG)  

The function is called    

[getGaussianKernel(shape, sigma)](https://github.com/ataffe/computer_vision/blob/master/4_Gaussian_Filter/Gaussian_Kernel.py)

where  

**shape** = A 2 element tuple which represents the size of the kernel  
**sigma** = The standard deviation of the gaussian distribution used to generate the kernel.  

Here is an example distribution created with a **sigma of 5** and **kernel size of 30x30** graphed using matplotlib's [plot.pyplot.imshow](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.imshow.html) function.  

![alt text](https://raw.github.com/ataffe/computer_vision/master/4_Gaussian_Filter/Gaussian_Kernel_S5.png)

To apply the kernel to the image I used the function:  

[image = filter2D(image, -1, kernel)](https://docs.opencv.org/2.4/modules/imgproc/doc/filtering.html#filter2d)

where   

**image** = the image that will blurred or convolved with the input kernel.  
**kernel** = the kernel that the image will be convolved with.  

# Blurred Image
(Kernel Size = 41   Sigma = 6)
![alt text](https://raw.github.com/ataffe/computer_vision/master/4_Gaussian_Filter/PeoriaCityHall_blur.jpg)

# Noise Image
(Sigma = 32)
![alt text](https://raw.github.com/ataffe/computer_vision/master/4_Gaussian_Filter/PeoriaCityHall_noisy.jpg)

# Original Image
![alt text](https://raw.github.com/ataffe/computer_vision/master/4_Gaussian_Filter/PeoriaCityHall.JPG)


