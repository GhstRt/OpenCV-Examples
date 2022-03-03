import cv2
import numpy as np

img = cv2.imread("../images/test2.png")
img = cv2.resize(img, (600, 600))
cv2.imshow("Orjinal", img)

print(img.shape)

pts1 = np.float32([[0, 0], [0, 600], [600, 0], [600, 600]])

pts2 = np.float32([[100, 50], [50, 600], [600, 50], [600, 600]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)

output = cv2.warpPerspective(img, matrix, dsize=(300, 300))

cv2.imshow("CIKTI", output)
cv2.waitKey(0)
