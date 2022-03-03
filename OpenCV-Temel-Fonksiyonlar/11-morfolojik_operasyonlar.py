import cv2
import numpy as np

img = cv2.imread("../images/test3.png")
img = cv2.resize(img, (600, 600))
cv2.imshow("Orjinal", img)

kernel = np.ones((5, 5), dtype=np.uint8)

# Erozyon
erozyon = img.copy()
erozyon = cv2.erode(erozyon, kernel, iterations=1)
cv2.imshow("EROZYON", erozyon)

# Genişleme
gen = img.copy()
gen = cv2.dilate(gen, kernel, iterations=1)
cv2.imshow("GENISLEME", gen)

# Açılma
ac = img.copy()
ac = cv2.morphologyEx(ac, cv2.MORPH_OPEN, kernel) # Önce erozyon sonra genişleme uygulanır.
cv2.imshow("ACILMA", ac)

# Kapatma
kap = img.copy()
kap = cv2.morphologyEx(kap, cv2.MORPH_CLOSE, kernel) # Önce genişleme sonra erozyon kullanılır.
cv2.imshow("KAPATMA", kap)

# Morfolojik Gradyan
grad = img.copy()
grad = cv2.morphologyEx(grad, cv2.MORPH_GRADIENT, kernel) # Görüntünün genişlemesi ve erozyonu arasındaki farktır.
cv2.imshow("MORFOLOJIK GRADYAN", grad)

cv2.waitKey(0)