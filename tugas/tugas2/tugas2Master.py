import cv2 as cv
import numpy as np
import os

# Import image
img = cv.imread("tugas/tugas2/tugas2.png")

# Blur the image
imgBlur = cv.GaussianBlur(img, (5, 5), 100)

# Define color bounds
lowerBound = np.array([0, 0, 90], dtype=np.uint8)
upperBound = np.array([20, 10, 105], dtype=np.uint8)

# Create a mask
mask = cv.inRange(imgBlur, lowerBound, upperBound)

# Find contours
contours, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
edges = 0
for contour in contours:
    area = cv.contourArea(contour)

    if area > 10000:
        cv.drawContours(img, [contour], -1, (255, 0, 0), 2)
        epsilon = 0.02 * cv.arcLength(contour, True)
        approx = cv.approxPolyDP(contour, epsilon, True)
        edges += len(approx)

cv.putText(img, str(edges), (10, 50), cv.FONT_HERSHEY_SIMPLEX , 2, (255, 0, 0), 2, cv.LINE_AA) 

# Display images
#cv.imshow("mask", mask)
cv.imshow("Original", img)

cd = 'tugas/tugas2'
os.chdir(cd)
cv.imwrite("done.jpg", img)

cv.waitKey(0)
cv.destroyAllWindows()
