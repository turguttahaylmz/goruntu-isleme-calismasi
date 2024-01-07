import cv2
import numpy as np

# İlk resmi oku
img1 = cv2.imread("siha.png")
# İkinci resmi oku
img2 = cv2.imread("iha.jpg")

# İki resmin boyutlarını eşleştir, ikinci resmi birinci resmin boyutlarına getir
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# Ağırlıklı toplama işlemi
alpha = 0.7
beta = 0.3
gamma = 0
toplam = cv2.addWeighted(img1, alpha, img2, beta, gamma)

# Sonucu göster
cv2.imshow("Ağırlıklı Toplama", toplam)
cv2.waitKey(0)
cv2.destroyAllWindows()



#img1 = cv2.resize(img1, (img2.shape[1], img2.shape[0])) 
# bu kod ile resimleri aynı Resimlerin boyutlarını ve kanal sayılarını  eşleştirmeniz gerekebilir veya 
# farklı boyutlardaki resimleri önce aynı boyuta getirmeniz gerekebilir. 
