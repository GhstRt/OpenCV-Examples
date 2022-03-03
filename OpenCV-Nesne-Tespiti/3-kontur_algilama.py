import cv2
import numpy as np

img = cv2.imread("../images/test3.png")
cv2.imshow("ORJINAL", img)

# Kontur Algılama
kontur = img.copy()
kontur = cv2.cvtColor(kontur, cv2.COLOR_BGR2GRAY)
(contours, _) = cv2.findContours(kontur, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
center = None

if len(contours) > 0:
    # en buyuk konturu al
    c = max(contours, key=cv2.contourArea)
    # dikdörtgene çevir
    rect = cv2.minAreaRect(c)

    ((x, y), (width, height), rotation) = rect

    s = "x: {}, y: {}, width: {}, height: {}, rotation: {}".format(np.round(x), np.round(y), np.round(width),
                                                                   np.round(height), np.round(rotation))
    print(s)

    # kutucuk
    box = cv2.boxPoints(rect)
    box = np.int64(box)

    # moment
    M = cv2.moments(c)
    center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

    cv2.drawContours(img, [box], 0, (0, 255, 255), 2)

    # merkere bir tane nokta çizelim: pembe
    cv2.circle(img, center, 5, (255, 0, 255), -1)

cv2.imshow("KONTUR ALGILAMA", img)

cv2.waitKey(0)