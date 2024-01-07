
import cv2
import numpy as np 
#sıfırlardan oluşan bir matris olursa siyah olacak 
img=np.zeros((512,512,3),np.uint8)#3 boyutlu olur
#resim üzerine çizgi çizmek için open cv hazır fonksiyonu line dır
#line fonksiyonu içine 5 paretmetre alır 1.neyin üzerine çizgi çizecek
#2 hangi noktadan başlayıp biteceği 
#3 renk koyu mavi için 255,0,0 veriyoruz 
#çizginin kalınlığı piksel olarak denk gelecek

cv2.line(img,(0,0),(511,511),(255,0,0),5) 
cv2.line(img,(50,400),(400,50),(0,255,0),10) 

cv2.imshow("resim",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

