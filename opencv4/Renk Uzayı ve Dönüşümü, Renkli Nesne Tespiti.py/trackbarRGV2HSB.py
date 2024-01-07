import cv2
import numpy as np

def nothing(x):
    pass

camera = cv2.VideoCapture(0)  # kameradan görüntü alıyorum

cv2.namedWindow("frame")
cv2.createTrackbar("H1", "frame", 0, 359, nothing)
cv2.createTrackbar("H2", "frame", 0, 359, nothing)
cv2.createTrackbar("S1", "frame", 0, 255, nothing)
cv2.createTrackbar("S2", "frame", 0, 255, nothing)
cv2.createTrackbar("V1", "frame", 0, 255, nothing)
cv2.createTrackbar("V2", "frame", 0, 255, nothing)

while camera.isOpened():
    _, frame = camera.read()  # normalde yandan ret koyarız ama fazla ram harcamasın diye koymuyoruz.

    # renk dönüşümü yapalım
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # frame resim demek
    H1 = cv2.getTrackbarPos("H1", "frame") / 2
    H2 = cv2.getTrackbarPos("H2", "frame") / 2
    S1 = cv2.getTrackbarPos("S1", "frame")
    S2 = cv2.getTrackbarPos("S2", "frame")
    V1 = cv2.getTrackbarPos("V1", "frame")
    V2 = cv2.getTrackbarPos("V2", "frame")

    lower = np.array([H1, S1, V1])  # H1 = Hue, S1 = Saturation, V1 = Value
    upper = np.array([H2, S2, V2])

    mask = cv2.inRange(hsv, lower, upper)  # maske yapalım

    res = cv2.bitwise_and(frame, frame, mask=mask)  # görüntüyü renkli görme

    cv2.imshow("frame", frame)  # önce olacak resmi
    cv2.imshow("hsv", mask)  # dönüştürdüğüm resmi

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
