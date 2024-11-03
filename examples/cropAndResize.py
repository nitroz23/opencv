import cv2 as cv

img = cv.imread("examples\img\yuuka.jpg")

#print(img.shape)
h, w, c = img.shape

croppedImg = img[500:1080, 225:600]
resizedImg = cv.resize(img, (int(w/2), int(h/2)))

cv.imshow("image", img)
cv.imshow("cropped", croppedImg)
cv.imshow("resized", resizedImg)

cv.waitKey(0)
cv.destroyAllWindows()