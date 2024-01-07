
import cv2
import numpy as np 
#sıfırlardan oluşan bir matris olursa siyah olacak 
img=np.zeros((512,512,3),np.uint8)#3 boyutlu olur

#resim,merkez,uzunluk,yay açısı başlangıç bitişi,rengi,kalınlığı içi dolu yapacaksan -1
cv2.ellipse(img,(256,256),(100,50),0,0,180,(255,100,0),3)
cv2.ellipse(img,(100,100),(100,50),0,0,180,(255,100,0),-1)
cv2.imshow("resim",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

