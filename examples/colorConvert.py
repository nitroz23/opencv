import cv2 as cv

img = cv.imread("examples\img\hoshino.jpg")

h, w, c = img.shape
resizedImg = cv.resize(img, (int(w/4), int(h/4)))

imgRGB = cv.cvtColor(resizedImg, cv.COLOR_BGR2RGB)
imgHSV = cv.cvtColor(resizedImg, cv.COLOR_BGR2HSV)

cv.imshow("org", resizedImg)
cv.imshow("RGB", imgRGB)
cv.imshow("HSV", imgHSV)

""" 
print("bgr: ")
print(resizedImg)
print("rgb: ")
print(imgRGB)
print("hsv: ")
print(imgHSV)
 """

cv.waitKey(0)
cv.destroyAllWindows()