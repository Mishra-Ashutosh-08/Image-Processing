import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../image/water.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32)/25

dst = cv2.filter2D(img, -1, kernel)#shows 2D effect
blur = cv2.blur(img, (5, 5))#Blurs the image
gblur = cv2.GaussianBlur(img, (5, 5), 0)
median = cv2.medianBlur(img, 5)#Smooth  the image
bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75)#Sharpens the Edge of image 

titles = ['image', '2D Convolution', 'blur', 'GaussianBlur', 'median', 'bilateralFilter']
images = [img, dst, blur, gblur, median, bilateralFilter]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
