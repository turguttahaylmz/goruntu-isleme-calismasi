import cv2
import numpy as np

# Giriş görüntüsünü yükleyin
img = cv2.imread("dron.jpg")

# Giriş görüntüsünün boyutlarını alın
rows, cols = img.shape[:2]

# Tıklama sayacını ve tıklamaların saklanacağı bir liste oluşturun
click_count = 0
a = []

# Görüntü penceresini oluşturun ve boyutunu ayarlayın
cv2.namedWindow("img", cv2.WINDOW_NORMAL)

# Hedef noktaları (dört köşe noktası) tanımlayın
dst_points = np.float32([
    [0, 0],
    [cols - 1, 0],
    [0, rows - 1],
    [cols - 1, rows - 1],
])

# Tıklama işlemini gerçekleştiren bir fonksiyon tanımlayın
def draw(event, x, y, flags, param):
    global click_count, a

    if event == cv2.EVENT_LBUTTONDBLCLK:
        # Çift tıklamada tıklama sayacını artırın ve tıklanan noktayı listeye ekleyin
        click_count += 1
        a.append([x, y])
        print("Click:", click_count, x, y)
        if click_count == 4:  # Dört noktayı seçtikten sonra
            # Dört noktayı kullanarak perspektif dönüşüm matrisini hesaplayın
            projective_matrix = cv2.getPerspectiveTransform(np.float32(a), dst_points)
            # Görüntüyü bu dönüşüm matrisi ile dönüştürün
            img_output = cv2.warpPerspective(img, projective_matrix, (cols, rows))
            # Dönüştürülmüş görüntüyü gösterin
            cv2.imshow("img_output", img_output)
    
# Tıklama işlevini ayarlayın
cv2.setMouseCallback("img", draw)

while True:
    # Giriş görüntüsünü gösterin
    cv2.imshow("img", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Pencereleri kapatın
cv2.destroyAllWindows()
