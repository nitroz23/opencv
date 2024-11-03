import cv2 as cv
import numpy as np

img = cv.imread("examples/img/blueRed.png")
imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)

lowerBound = np.array([0, 0, 0], dtype = np.uint8)
upperBound = np.array([10, 255, 255], dtype = np.uint8)
mask = cv.inRange(imgHSV, lowerBound, upperBound)
bitwiseAND = cv.bitwise_and(img, img, mask=mask)

cv.imshow("mask", mask)
cv.imshow("and", bitwiseAND)
cv.waitKey(0)
cv.destroyAllWindows()