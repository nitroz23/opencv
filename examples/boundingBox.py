import cv2 as cv
import numpy as np

img = cv.imread("examples\img\momoiMidori.jpg")
h, w, c = img.shape
resizedImg = cv.resize(img, (int(w/4), int(h/4)))

lowerBound = np.array([150, 150, 250], dtype = np.uint8)
upperBound = np.array([180, 180, 255], dtype = np.uint8)

mask = cv.inRange(resizedImg, lowerBound, upperBound)
contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

for contour in contours:
    x, y, w, h = cv.boundingRect(contour)
    area = cv.contourArea(contour)

    if area > 500:
        color = (0, 0, 255)  
        thickness = 2
        cv.rectangle(resizedImg, (x, y), (x + w, y + h), color, thickness)

#cv.imshow("mask", mask)
cv.imshow("test", resizedImg)
cv.waitKey(0)
cv.destroyAllWindows()