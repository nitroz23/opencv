import cv2 as cv

cam = cv.VideoCapture(0)

while True:
    ret, frame = cam.read()

    if not ret: break

    cv.imshow('WEBCAM', frame)

    if cv.waitKey(1) == ord('a'): break

cam.release()
cv.destroyAllWindows()