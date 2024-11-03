import cv2 as cv

img = cv.imread("examples\img\shrek.jpeg")

gauss = cv.GaussianBlur(img, (7, 7), 0) 
median = cv.medianBlur(img, 5) 
bilateral = cv.bilateralFilter(img, 9, 75, 75) 

cv.imshow('org', img)
cv.imshow('Gaussian Blurring', gauss) 
cv.imshow('Median Blurring', median) 
cv.imshow('Bilateral Blurring', bilateral) 

cv.waitKey(0) 
cv.destroyAllWindows() 