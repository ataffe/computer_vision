#Image Difference

import numpy as np
import cv2
from matplotlib import pyplot as plt

imageName1 = 'Mount_Fuji.jpg'
imageName2 = 'ocean.jpg'


#load a color image in grayscale
image1 = cv2.imread(imageName1, 0)
image2 = cv2.imread(imageName2, 0)

#print the image size
print("Shape img 1: " + str(image1.shape))
print("Shape img 2: " + str(image2.shape))


#resize the images to be the same size
image1 = image1[:803,:1920]
image2 = image2[:803,:1200]

cv2.imshow(imageName2[:-4], image2)
cv2.waitKey(0)
cv2.destroyAllWindows()