
import cv2
import numpy as np 
#sıfırlardan oluşan bir matris olursa siyah olacak 
img=np.zeros((512,512,3),np.uint8)#3 boyutlu olur
#resim üzerine çizgi çizmek için open cv hazır fonksiyonu line dır
#line fonksiyonu içine 5 paretmetre alır 1.neyin üzerine çizgi çizecek
#2 hangi noktadan başlayıp biteceği 
#3 renk koyu mavi için 255,0,0 veriyoruz 
#çizginin kalınlığı piksel olarak denk gelecek

cv2.rectangle(img,(50,50),(300,300),(0,0,255),5 )
cv2.rectangle(img,(300,300),(511,511),(0,0,255),-1 )
#resim,dikdörtgenin başlayacığı koordinat,renk,kalınlık içini doldukmak için de -1 yazarız 
cv2.imshow("resim",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

