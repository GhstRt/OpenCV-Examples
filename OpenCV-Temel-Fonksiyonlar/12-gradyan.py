import cv2

img = cv2.imread("../images/test4.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("ORJINAL", img)

# Sobel fonksiyonu hem dikey hem de yatay kenarları tespit edebiliyor. Bunu dx ve dy parametreleriyle ayarlıyoruz.
sobelx = cv2.Sobel(img, ddepth=cv2.CV_16S, dx=1, dy=0, ksize=5)
cv2.imshow("DIK KENARLAR", sobelx)

sobely = cv2.Sobel(img, ddepth=cv2.CV_16S, dx=0, dy=1, ksize=5)
cv2.imshow("YATAY KENARLAR", sobely)

# Laplacian fonksiyonu iki yönlü çalışıyor yani hem dikey hem de yatay kenarı aynı anda tespit edebiliyor.
laplacian = cv2.Laplacian(img, ddepth=cv2.CV_16S)
cv2.imshow("IKI YONLU", laplacian)

cv2.waitKey(0)