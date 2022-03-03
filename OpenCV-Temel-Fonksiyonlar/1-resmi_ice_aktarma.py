import cv2

# Verilen dizindeki resmi numpy dizisi olarak içeri aktarır.
img = cv2.imread("../images/test.png")

print(type(img))
print(img.shape)

# Resmi görüntülemeyi sağlar.
cv2.imshow("TEST", img)

# Herhangi bir tuşa basılana kadar yukarıda görüntülemeye aldığımız resmi göstermeye devam eder.
cv2.waitKey(0)

# Tüm pencereleri temizler.
cv2.destroyAllWindows()

