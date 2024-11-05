import cv2 as cv
import numpy as np

img = cv.imread("tugas/tugas1/tugas1.jpg")

# Define character data with color bounds, area thresholds, and labels
characters = [
    {"name": "Iroha", "lower": [120, 85, 180], "upper": [140, 100, 222], "area_thresh": 2000, "color": (0, 0, 255)},
    {"name": "Ibuki", "lower": [160, 225, 250], "upper": [185, 250, 255], "area_thresh": 3000, "color": (0, 230, 250)},
    {"name": "Hina", "lower": [250, 220, 235], "upper": [255, 240, 250], "area_thresh": 3000, "color": (90, 35, 75)},
    {"name": "Makoto", "lower": [200, 215, 215], "upper": [220, 230, 230], "area_thresh": 3000, "color": (180, 180, 200)},
]

for char in characters:
    # Create mask and find contours for each character
    lower_bound = np.array(char["lower"], dtype=np.uint8)
    upper_bound = np.array(char["upper"], dtype=np.uint8)
    mask = cv.inRange(img, lower_bound, upper_bound)
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv.contourArea(contour)
        if area > char["area_thresh"]:
            x, y, w, h = cv.boundingRect(contour)
            cv.rectangle(img, (x, y), (x + w, y + h), char["color"], 5)
            cv.putText(img, char["name"], (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 1, char["color"], 2, cv.LINE_AA)

# Display the result
cv.imshow("test", img)
cv.waitKey(0)
cv.destroyAllWindows()
