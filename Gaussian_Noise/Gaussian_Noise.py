#Gaussian Noise

import numpy as np
import cv2
from matplotlib import pyplot as plt

imageName1 = "grand.jpg"
imageName2 = "noisy.jpg"
displayMatplot = False

#Generate noise and add it to an image. The noise is from a random normal distribution. 
def addGaussianNoise(img1, sigma):
    rows = img1.shape[0]
    columns = img1.shape[1]
    noise = np.random.normal(0,sigma ,(rows,columns))
    noise = noise.astype(int)
    return img1 + noise


image1 = cv2.imread(imageName1, 0)
print("Shape img 1: " + str(image1.shape))
image1 = image1[100:1900,800:2100]
noisyImage = addGaussianNoise(image1, 32)
cv2.imwrite(imageName2 ,noisyImage)

if displayMatplot:
    plt.imshow(image1, cmap = 'gray', interpolation= 'bicubic', shape=(image1.shape[0],image1.shape[1]))
    plt.xticks([]), plt.yticks([]) #to hide tick values on X and Y axis
    plt.show()
else:
    cv2.imshow(imageName2, np.array(noisyImage, dtype=np.uint8 ) )
    cv2.imshow(imageName1, np.array(image1, dtype=np.uint8 ) )
    cv2.waitKey(0)
    cv2. destroyAllWindows()
