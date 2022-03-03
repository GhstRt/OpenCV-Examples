import cv2

img = cv2.imread("../images/test5.png")
cv2.imshow("ANA RESIM", img)

sablon = cv2.imread("../images/test6.png")
cv2.imshow("SABLON RESIM", sablon)
print(sablon.shape)
h, w, _ = sablon.shape

sonuc = cv2.matchTemplate(img, sablon, cv2.TM_CCORR)
min_deg, max_deg, min_loc, max_loc = cv2.minMaxLoc(sonuc)
print(min_deg, max_deg, min_loc, max_loc)

top_left = max_loc
bottom_right = (top_left[0]+w, top_left[1]+h)

cv2.rectangle(img, top_left, bottom_right, (255, 0, 0), 2)

cv2.imshow("SONUC", img)

cv2.waitKey(0)