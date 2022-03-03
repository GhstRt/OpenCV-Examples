import cv2
import numpy as np

# kırmızı renk aralığı HSV
redLower = (28, 32, 0)
redUpper = (240,235,240)

for i in range(1):

    success = 1
    imgOriginal = cv2.imread("../images/test5.png")
    if success:

        # blur
        blurred = cv2.GaussianBlur(imgOriginal, (11, 11), 0)

        # hsv
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        cv2.imshow("HSV Image", hsv)

        # mavi için maske oluştur
        mask = cv2.inRange(hsv, redLower, redUpper)
        cv2.imshow("mask Image", mask)
        # maskenin etrafında kalan gürültüleri sil
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        cv2.imshow("Mask + erozyon ve genisleme", mask)

        # farklı sürüm için
        # (_, contours,_) = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # kontur
        (contours, _) = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        center = None

        if len(contours) > 0:
            for g in range(len(contours)):
                # en buyuk konturu al
                c = contours[g] #max(contours, key=cv2.contourArea)

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

                # konturu çizdir: sarı
                cv2.drawContours(imgOriginal, [box], 0, (0, 255, 255), 2)

                # merkere bir tane nokta çizelim: pembe
                cv2.circle(imgOriginal, center, 5, (255, 0, 255), -1)

                # bilgileri ekrana yazdır
                cv2.putText(imgOriginal, s, (25, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 2)

            cv2.imshow("Orijinal Tespit", imgOriginal)
            cv2.waitKey(0)

        if cv2.waitKey(1) & 0xFF == ord("q"): break