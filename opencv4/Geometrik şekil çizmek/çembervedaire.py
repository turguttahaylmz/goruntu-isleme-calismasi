
import cv2
import numpy as np 
#sıfırlardan oluşan bir matris olursa siyah olacak 
img=np.zeros((512,512,3),np.uint8)#3 boyutlu olur

#ilk görüntü ikincidairenin merkezi üçüncü yarıçapı,4 renk ,kalınlık  daire yappınca -1 yap
cv2.circle(img,(255,255),60,(120,120,120),2)

cv2.circle(img,(100,100),90,(255,50,50),-1)

cv2.imshow("resim",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

