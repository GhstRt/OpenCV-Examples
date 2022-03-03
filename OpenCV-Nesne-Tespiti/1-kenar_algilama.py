import cv2

img = cv2.imread("../images/test2.png")
img = cv2.resize(img, (600, 600))
cv2.imshow("ORJINAL", img)

kenar = img.copy()
kenar = cv2.Canny(kenar, 100, 200) # Kenarları algılamak için kullanılan fonksiyon.
cv2.imshow("KENAR ALGILAMA", kenar)

cv2.waitKey(0)