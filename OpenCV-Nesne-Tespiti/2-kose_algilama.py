import cv2
import numpy as np

img = cv2.imread("../images/test3.png")
img = cv2.resize(img, (600, 600))
cv2.imshow("ORJINAL", img)

# Harris Corner Yöntemi
har = img.copy()
corner = img.copy()
har = cv2.cvtColor(har, cv2.COLOR_BGR2GRAY)
har = cv2.cornerHarris(src=har, blockSize=2, ksize=3, k=0.04)
har = cv2.dilate(har, None)
corner[har>0.2*har.max()] = [0,0,255]

cv2.imshow("HARRIS CORNER", corner)

# Shi Tamsai Yöntemi
shi = img.copy()
shi = cv2.cvtColor(shi, cv2.COLOR_BGR2GRAY)
corners = img.copy()
shi = cv2.goodFeaturesToTrack(shi, maxCorners=20, qualityLevel=0.01, minDistance=1)
shi = np.int64(shi)

for i in shi:
    x, y = i.ravel()
    cv2.circle(corners, (x, y), 2, (0, 255, 0), cv2.FILLED)

cv2.imshow("SHI TAMSAI", corners)

cv2.waitKey(0)