import cv2
import numpy as np

img = cv2.imread("dron.jpg")

# Görüntünün satır ve sütun bilgilerini alın
rows, cols, _ = img.shape  # Renkli bir görüntü olduğu için 3 kanalı (BGR) vardır.

#shape özelliği, bir Numpy dizisinin boyutunu, yani kaç satır ve sütun içerdiğini belirtir.
#  #Dizi 2D (iki boyutlu) bir dizi ise, "shape" özelliği iki değer içerir: satır sayısı ve sütun sayısı. 
#Eğer 3D bir dizi ise, "shape" özelliği üç değer içerir: yükseklik (satır sayısı), genişlik (sütun sayısı) ve 
#kanal sayısı (örneğin, renkli bir görüntüde genellikle 3 kanal vardır: mavi, yeşil ve kırmızı).

# Kaydırma matrisini oluşturun
translation_matrix = np.float32([[1, 0, 50], [0, 1, 50]])  # x ekseninde 50, y ekseninde 50 birim kaydırma

# Kaydırma işlemi yaparak yeni görüntüyü oluşturun
img_translation = cv2.warpAffine(img, translation_matrix, (cols, rows))

# Görüntüleri göster
cv2.imshow("img", img)
cv2.imshow("img_translation", img_translation)
cv2.waitKey(0)
cv2.destroyAllWindows()
