import cv2

img = cv2.imread("../images/test2.png")
img = cv2.resize(img, (600, 600))
cv2.imshow("Orjinal", img)

# Ortalama Bulanıklaştırma
dst = img.copy()
dst = cv2.blur(dst, ksize=(4, 4))
cv2.imshow("ORTALAMA", dst)

# Gauss Bulanıklaştırma
gb = img.copy()
gb = cv2.GaussianBlur(gb, ksize=(3, 3), sigmaX=7)
cv2.imshow("GAUSS", gb)

# Meydan Bulanıklaşırma
mb = img.copy()
mb = cv2.medianBlur(mb, ksize=3)
cv2.imshow("MEDYAN", mb)

cv2.waitKey(0)