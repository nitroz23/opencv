import cv2 as cv
import os

cd = 'tugas/tugas2'
print(os.listdir(cd))

img = cv.imread("tugas/tugas2/bi0o1d5qw7y21.jpeg")

#print(img.shape)
h, w, c = img.shape

croppedImg = img[500:1080, 225:600]
resizedImg = cv.resize(img, (int(w/2), int(h/2)))

cv.imshow("image", img)
cv.imshow("cropped", croppedImg)
cv.imshow("resized", resizedImg)

os.chdir(cd)
cv.imwrite("test.jpg", resizedImg)

cv.waitKey(0)
cv.destroyAllWindows()