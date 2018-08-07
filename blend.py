#Blend

import numpy as np 
import cv2
from matplotlib import pyplot as plt

imageName1 = 'mountain.jpg'
imageName2 = 'lena.jpg'
imageName3 = 'blended.jpg'

displayMatplot = False
display = True

# Blend accomplished using the equation:
# alpha = percent of blend
# g(x) = (1 - alpha)img2 + (alpha)img2
def blend(alpha, img1, img2):
    compPercent = 1 - alpha
    #img1 = img1 * alpha
    #img2 = img2 *compPercent
    #blendedImage = img1 + img2
    blendedImage = cv2.addWeighted(img1,alpha,img2,compPercent,0)

    return (blendedImage)



#load a color image in grayscale
image1 = cv2.imread(imageName1, 0)
image2 = cv2.imread(imageName2, 0)

print("Shape img 1: " + str(image1.shape))
print("Shape img 2: " + str(image2.shape))

image1 = image1[200:1400,200:1900]
image2 = image2[200:1400,200:1900]

image3 = blend(.70,image1,image2)
print("Shape img 3: " + str(image3.shape))

cv2.imwrite(imageName3[:-4] + str('_gray.jpg'),image3)

if display:
    if not displayMatplot:
        cv2.imshow(imageName3, image3)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        plt.imshow(image3,cmap = 'gray', interpolation = 'bicubic', shape=(1400,1900))
        plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
        plt.show()

