import numpy as np
import cv2
from matplotlib import pyplot as plt
import threading
from tkinter import *

imageName = "PeoriaCityHall.JPG"
image = cv2.imread(imageName, 0)
root = Tk()
blurSigma = DoubleVar()
noiseSigma = DoubleVar()
kernelSize = IntVar()

#Generate noise and add it to an image. The noise is from a random normal distribution. 
def addGaussianNoise(img1, sigma):
    rows = img1.shape[0]
    columns = img1.shape[1]
    noise = np.random.normal(0,sigma ,(rows,columns))
    noise = noise.astype(int)
    return img1 + noise

noisyImage = addGaussianNoise(image,32)

class filterThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        displayFilter()


#Remove noise hsize = 31, sigma = 5
def removeNoiseGaussian(img, hsize=1023, sigma=5):
    kernel = cv2.getGaussianKernel(hsize,sigma)
    img = np.array(img, dtype=np.uint8)
    img = cv2.filter2D(img, -1, kernel)
    return img


def displayFilter():
    while(True):
        noisyImage = addGaussianNoise(image,noiseSigma.get())
        blurImage = removeNoiseGaussian(noisyImage,hsize=kernelSize.get(), sigma=blurSigma.get())
        cv2.imshow( blurImageName, np.array(blurImage, dtype=np.uint8 ) )

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            cv2.imwrite(noisyImageName, noisyImage)
            cv2.imwrite(blurImageName, blurImage)
            break

def showSlideBar():
    bar1 = Scale(root, from_=1, to=70, orient=HORIZONTAL, variable=blurSigma, length=200)
    bar2 = Scale(root, from_=1, to=70, orient=HORIZONTAL, variable=noiseSigma, length=200)
    bar3 = Scale(root, from_=31, to=1023, orient=HORIZONTAL, variable=kernelSize, resolution=2, length=200)

    bar1.pack()
    bar2.pack()
    bar3.pack()

    bar1 = Label(root, text= "Blur Sigma Adjustment (Top)")
    bar2 = Label(root, text= "Noise Sigma Adjustment (Middle)")
    bar3 = Label(root, text= "Kernel Size Adjustment (Bottom)")
    
    bar3.pack()
    bar2.pack()
    bar1.pack()
    root.mainloop()


noisyImageName = imageName[:-4] + "_noisy.jpg"
blurImageName = imageName[:-4] + "_blur.jpg"

#display()
thread1 = filterThread(1, "display thread", 1)

try:
    #theading.Thread(target=display).start()
    thread1.start()
    showSlideBar()
    thread1.join()
except:
    print("Error: unable to start thread")




