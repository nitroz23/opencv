import cv2 as cv
import numpy as np
import os

img = cv.imread("tugas/tugas1/tugas1.jpg")

lowerBoundIroha = np.array([120, 85, 180], dtype = np.uint8)
upperBoundIroha = np.array([140, 100, 222], dtype = np.uint8)
lowerBoundIbuki = np.array([160, 225, 250], dtype = np.uint8)
upperBoundIbuki = np.array([185, 250, 255], dtype = np.uint8)
lowerBoundHina = np.array([250, 220, 235], dtype = np.uint8)
upperBoundHina = np.array([255, 240, 250], dtype = np.uint8)
lowerBoundMakoto = np.array([200, 215, 215], dtype = np.uint8)
upperBoundMakoto = np.array([220, 230, 230], dtype = np.uint8)

maskIroha = cv.inRange(img, lowerBoundIroha, upperBoundIroha)
contoursIroha, _ = cv.findContours(maskIroha, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

maskIbuki = cv.inRange(img, lowerBoundIbuki, upperBoundIbuki)
contoursIbuki, _ = cv.findContours(maskIbuki, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

maskHina = cv.inRange(img, lowerBoundHina, upperBoundHina)
contoursHina, _ = cv.findContours(maskHina, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

maskMakoto = cv.inRange(img, lowerBoundMakoto, upperBoundMakoto)
contoursMakoto, _ = cv.findContours(maskMakoto, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

for contour in contoursIroha:
    x, y, w, h = cv.boundingRect(contour)
    area = cv.contourArea(contour)

    if area > 2000:
        color = (0, 0, 255)  
        thickness = 5
        cv.rectangle(img, (x, y), (x + w, y + h), color, thickness)
        cv.putText(img, "Iroha", (x , y - 10), cv.FONT_HERSHEY_SIMPLEX , 1 , color, 2, cv.LINE_AA)

for contour in contoursIbuki:
    x, y, w, h = cv.boundingRect(contour)
    area = cv.contourArea(contour)

    if area > 3000:
        color = (0, 230, 250)  
        thickness = 5
        cv.rectangle(img, (x, y), (x + w, y + h), color, thickness)
        cv.putText(img, "Ibuki", (x , y - 10), cv.FONT_HERSHEY_SIMPLEX , 1 , color, 2, cv.LINE_AA)

for contour in contoursHina:
    x, y, w, h = cv.boundingRect(contour)
    area = cv.contourArea(contour)

    if area > 3000:
        color = (90, 35, 75)  
        thickness = 5
        cv.rectangle(img, (x, y), (x + w, y + h), color, thickness)
        cv.putText(img, "Hina", (x , y - 10), cv.FONT_HERSHEY_SIMPLEX , 1 , color, 2, cv.LINE_AA)

for contour in contoursMakoto:
    x, y, w, h = cv.boundingRect(contour)
    area = cv.contourArea(contour)

    if area > 3000:
        color = (180, 180, 200)  
        thickness = 5
        cv.rectangle(img, (x, y), (x + w, y + h), color, thickness)
        cv.putText(img, "Makoto", (x , y - 10), cv.FONT_HERSHEY_SIMPLEX , 1 , color, 2, cv.LINE_AA)

cd = 'tugas/tugas1'
os.chdir(cd)

cv.imshow("maskIroha", maskIroha)
cv.imshow("maskIbuki", maskIbuki)
cv.imshow("maskHina", maskHina)
cv.imshow("maskMakoto", maskMakoto)
cv.imshow("test", img)
cv.imwrite("done.jpg", img)
cv.waitKey(0)
cv.destroyAllWindows()