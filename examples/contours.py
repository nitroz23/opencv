import cv2 as cv

img = cv.imread("examples\img\hoshino.jpg")
h, w, c = img.shape
resizedImg = cv.resize(img, (int(w/2), int(h/2)))

imgBlur = cv.GaussianBlur(resizedImg, (5, 5), 0)
canny = cv.Canny(imgBlur, 125, 175)

contours, hierarchy = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
print(f"number of contours: {len(contours)}")

cv.drawContours(img, contours, -1, (0, 0, 255) , 2)

cv.imshow("org", resizedImg)
cv.imshow("result", canny)

cv.waitKey(0)
cv.destroyAllWindows()