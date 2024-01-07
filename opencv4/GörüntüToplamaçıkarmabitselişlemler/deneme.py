import cv2

img1 = cv2.imread("siha.png")
img2 = cv2.imread("iha.jpg")

# İlk resmin boyutları
x, y, z = img1.shape

# İkinci resmi kırp
roi = img2[0:x, 0:y]

# İlk resmi gri tona döndür
img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

# Gri resme bir eşik değeri uygula
ret, mask = cv2.threshold(img1_gray, 10, 255, cv2.THRESH_BINARY)

# Gri resmin boyutunu, ROI'nin boyutuna uygun olarak yeniden boyutlandır
mask = cv2.resize(mask, (y, x))

# Maskenin tersini al
mask_inv = cv2.bitwise_not(mask)

# ROI ve maskenin tersi arasındaki kısmı hesapla
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

# İlk resmin ROI'si ile maskenin arasındaki kısmı hesapla
img1_fg = cv2.bitwise_and(img1, img1, mask=mask)

# İki görüntüyü topla
toplam = cv2.add(img1_bg, img1_fg)

# Toplamı ikinci resmin ROI'sine yerleştir
img2[0:x, 0:y] = toplam

# Pencereleri göster
cv2.namedWindow("resim", cv2.WINDOW_NORMAL)
cv2.imshow("resim", img2)
cv2.imshow("resim2", toplam)
cv2.waitKey(0)
cv2.destroyAllWindows()
