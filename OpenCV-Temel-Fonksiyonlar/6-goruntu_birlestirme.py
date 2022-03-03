import cv2
import numpy as np

img = cv2.imread("../images/test2.png")
img = cv2.resize(img, (300, 300))
cv2.imshow("Orjinal", img)

hs = np.hstack((img, img)) # İki numpy dizisini yatay olarak bir birine ekler.
cv2.imshow("YATAY", hs)

vs = np.vstack((img, img)) # İki numpy dizisini dikey olarak birbirine ekler.
cv2.imshow("DIKEY", vs)

cv2.waitKey(0)