import cv2 as cv

img = cv.imread("examples\img\clevelandILY.jpeg")
cv.imshow("image", img)

cv.waitKey(0)
cv.destroyAllWindows()
