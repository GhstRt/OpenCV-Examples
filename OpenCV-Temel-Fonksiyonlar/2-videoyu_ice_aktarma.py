import cv2
import time

# Verilen dizindeki resmi numpy dizisi olarak içeri aktarır.
cap = cv2.VideoCapture("../images/test.mp4")

print(type(cap))

# Oluşturduğumuz cap nesnesinin get adlı fonksiyonu nesne ile ilgili özelliklerin çağırılması için kullanılır.
print("Genişlik: ", cap.get(3)) # Videonun genişliğini döndürür.
print("Yükseklik: ", cap.get(4)) # Videonun yüksekliğini döndürür.

while cap.isOpened(): # Videonun açılabilir olup olmadığını kotrol eder.

    ret, frame = cap.read() # ret değişkeni karenin doğru alınıp alınamadığına dair True/False şeklinde çıktı döndürür.

    if ret: # Karenin doğru alındığını kontrol ediyoruz.
        time.sleep(0.01) # Eğer burada bir bekleme süresi koymazsak video çok hızlı akacaktır.
        cv2.imshow("TEST VIDEO", frame)

    else: break

    if cv2.waitKey(1) & 0xFF == ord("q"): # Eğer q tuşuna basılırsa video döngüsü kırılır.
        break

cap.release() # Bu fonksiyon video kaydını sonlandırır.
cv2.destroyAllWindows()
