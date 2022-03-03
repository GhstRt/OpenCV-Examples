import cv2

# Bu kısımda verdiğimiz 0 değeri kameranın indexidir. Eğer 2 kamera takılı olsaydı ve 2. kamerayı seçecek olsaydık 1 yazardık.
cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # Kameranın döndürdüğü Genişlik değeri
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # Kameranın döndürdüğü Yükseklik değeri

# Video kaydı için nesne oluşturduk. Parametreler sırasıyla (isim, kodek, fps, (en, boy)) şeklindedir.
writer = cv2.VideoWriter("video.mp4", cv2.VideoWriter_fourcc(*"MP4V"), 30, (width, height))

while True:
    ret, frame = cap.read()

    if ret:
        cv2.imshow("KAMERA", frame)
        writer.write(frame)

    if cv2.waitKey(1) & 0xFF == ord("q"): break

cap.release()
writer.release()
cv2.destroyAllWindows()