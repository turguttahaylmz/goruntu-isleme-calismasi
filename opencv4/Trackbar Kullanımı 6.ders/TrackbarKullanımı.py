import cv2
import numpy as np 


def nothing(x):
    pass


img=np.zeros((512,512,3),np.uint8)

cv2.namedWindow("resim")

cv2.createTrackbar("R","resim",0,255,nothing)#hazır fonksiyon kullanıyoruz.
cv2.createTrackbar("G","resim",0,255,nothing)
cv2.createTrackbar("B","resim",0,255,nothing)

while True:
    cv2.imshow("resim", img)
    key = cv2.waitKey(1)
    
    if key == ord("q"):
        break

cv2.destroyAllWindows()