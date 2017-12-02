# This program prints Hello, world!
# print('Hello, world!')

#OpenCV data types
# Numpy (for numerical calculations)
# Matplotlib (for plotting)
import cv2
import numpy as np
from matplotlib import pyplot as plt

#read in image then change to BGR 2 GREY
img = cv2.imread('dog.jpg',)
imgGray = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY )

#cv2.imwrite( "grey.png", img )
#cv2.imshow( "grey.png", img )

#holds image (display for user)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

imgOut = cv2.GaussianBlur(imgGray,(3, 3),0)
imgOut2 = cv2.GaussianBlur(imgGray,(13, 13),0)

sobelHorizontal = cv2.Sobel(imgGray,cv2.CV_64F,1,0,ksize=5) # x dir
sobelVertical = cv2.Sobel(imgGray,cv2.CV_64F,0,1,ksize=5) # y dir


#canny = cv2.Canny(imgGray,50,100)

sobelSum =cv2.add(sobelHorizontal,sobelVertical)

#sobelSum2 =cv2.add(sobelSum,canny)
#theSum = sum(sobelSum(:))

ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

#if (img[i][j]>200){ 
 #   newImg[i][j] =1
#}
#myNewImg
#else{}


#if img(i, j) > thresh{
#    newImg(i, j) = maxValue
#}
#myNewImg
#else{
 #   newImg(i, j)= 0
#}
#thresh = 200
#maxValue = 255

#th1,newImg = cv2.threshold(img,thresh, maxValue,cv2.THRESH_BINARY)

nrows =2
ncols =4


plt.subplot(nrows, ncols,1),plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB), cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(nrows, ncols,2),plt.imshow(imgGray, cmap = 'gray')
plt.title('GrayScale'), plt.xticks([]), plt.yticks([])

plt.subplot(nrows, ncols,3),plt.imshow(imgOut, cmap ='gray')
plt.title('3x3 Blur'), plt.xticks([]), plt.yticks([])

plt.subplot(nrows, ncols,4),plt.imshow(imgOut2, cmap ='gray')
plt.title('13X13 Blur'), plt.xticks([]), plt.yticks([])

plt.subplot(nrows, ncols,5),plt.imshow(sobelHorizontal, cmap ='gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])

plt.subplot(nrows, ncols,6),plt.imshow(sobelVertical, cmap ='gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.subplot(nrows, ncols,7),plt.imshow(sobelSum, cmap ='gray')
plt.title('Sobel Sum'), plt.xticks([]), plt.yticks([])

plt.subplot(nrows, ncols,8),plt.imshow(th1, cmap ='gray')
plt.title('SS Threshold'), plt.xticks([]), plt.yticks([])

#plt.subplot(nrows, ncols,8),plt.imshow(canny, cmap ='gray')
#plt.title('Canny Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()


