import cv2

img = cv2.imread("../images/test2.png")
img = cv2.resize(img, (600, 600))
cv2.imshow("Orjinal", img)

line = img.copy()
cv2.line(line, pt1=(10, 50), pt2=(100,200), color=(0, 255, 0), thickness=2) # Bir koordinattan diğer bir koordinata çizgi çekmeyi sağlar
cv2.imshow("Çizgi", line)

rectangle = img.copy()
cv2.rectangle(rectangle, (10, 50), (100, 200), (0, 255, 0), cv2.FILLED) # Bir koordinatı sol üst diğer bir koordinatı sağ alt olarak alır.
cv2.imshow("Dikdörtgen", rectangle)

circle = img.copy()
cv2.circle(circle, (100, 200), 50, (0, 255, 0), 10) # Merkez koordinatı verilir ardından yarıçap belirtilerek çember çizilir.
cv2.imshow("Çember", circle)

text = img.copy()
cv2.putText(text, "Hello World!", (100, 200), cv2.FONT_HERSHEY_PLAIN, 5, (0, 255, 0), 10) # Verilen noktadan başlayarak yazıyı resme işler.
cv2.imshow("Yazı", text)


cv2.waitKey(0)