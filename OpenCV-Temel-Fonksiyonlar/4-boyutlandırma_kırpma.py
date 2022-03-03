import cv2

img = cv2.imread("../images/test2.png")
print("Orjinal: ", img.shape)
cv2.imshow("ORJINAL", img)


boyut = img.copy() # Orjinal resim üzerinde işlem yapmamak için copy() fonksiyonu ile orjinal resmi kopyalıyoruz.
boyut = cv2.resize(boyut, dsize=(300, 300)) # Resmi yeniden boyutlandırmak için kullanılan fonksiyon.
print("Yeniden Boyutlandırma: ", boyut.shape)
cv2.imshow("YENIDEN BOYUTLANDIRMA", boyut)


kirpma = img.copy()
kirpma = kirpma[:200, :200] # Hem yüksekliği hem de genişliği 0'dan 300. pixele kadar alıyoruz.
print("Kırpma: ", kirpma.shape)
cv2.imshow("KIRPMA", kirpma)

cv2.waitKey(0)
