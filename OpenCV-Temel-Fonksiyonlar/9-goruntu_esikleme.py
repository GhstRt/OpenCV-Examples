import cv2

img = cv2.imread("../images/test2.png")
img = cv2.resize(img, (600, 600))
cv2.imshow("Orjinal", img)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, threshimg = cv2.threshold(img, 35, 255, cv2.THRESH_BINARY) # Thresholding işlemini uygulayan fonksiyon

cv2.imshow("THRESHOLD", threshimg)

cv2.waitKey(0)

