import cv2

img = cv2.imread("../images/test2.png")
img = cv2.resize(img, (600, 600))
img1 = cv2.imread("../images/test.png")
img1 = cv2.resize(img1, (600, 600))

cv2.imshow("Orjinal-1", img)
cv2.imshow("Orjinal-2", img1)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Resmin renk skalasını BGR'dan RGB'ye çevirdik
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB) # Aynı işlemi burada da uyguluyoruz.

blended = cv2.addWeighted(src1=img, alpha=0.5, src2=img1, beta=0.5, gamma=0) # İki resmi karıştırmak için kullandığımız fonksiyon.
cv2.imshow("KARISTIR", blended)

cv2.waitKey(0)
