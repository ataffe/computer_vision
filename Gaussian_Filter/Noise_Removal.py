import numpy as np
import cv2
from matplotlib import pyplot as plt


imageName = "PeoriaCityHall.JPG"

#Remove noise hsize = 31, sigma = 5
def removeNoiseGaussian(img, hsize=1023, sigma=5):
    kernel = cv2.getGaussianKernel(hsize,sigma)
    img = np.array(img, dtype=np.uint8)
    img = cv2.filter2D(img, -1, kernel)
    return img


#Generate noise and add it to an image. The noise is from a random normal distribution. 
def addGaussianNoise(img1, sigma):
    rows = img1.shape[0]
    columns = img1.shape[1]
    noise = np.random.normal(0,sigma ,(rows,columns))
    noise = noise.astype(int)
    return img1 + noise

image = cv2.imread(imageName, 0)
print("Shape image 1; " + str(image.shape))
noisyImage = addGaussianNoise(image,32)
blurImage = removeNoiseGaussian(noisyImage)

noisyImageName = imageName[:-4] + "_noisy.jpg"
blurImageName = imageName[:-4] + "_blur.jpg"

cv2.imwrite(noisyImageName, noisyImage)
cv2.imwrite(blurImageName, blurImage)

fig = plt.figure(figsize=plt.figaspect(0.5))
ax = fig.add_subplot(1,2,1, projection='3d')




cv2.imshow( noisyImageName, np.array(noisyImage, dtype=np.uint8 ) )
cv2.imshow( blurImageName, np.array(blurImage, dtype=np.uint8 ) )
cv2.imshow( imageName, np.array(image, dtype=np.uint8 ) )
cv2.waitKey(0)
cv2.destroyAllWindows()


