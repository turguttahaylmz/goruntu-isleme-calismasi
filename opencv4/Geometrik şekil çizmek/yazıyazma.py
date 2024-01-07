
import cv2
import numpy as np 
#sıfırlardan oluşan bir matris olursa siyah olacak 
img=np.zeros((512,512,3),np.uint8)#3 boyutlu olur

#ilk göresel 2 yazının ne olduğu 3sol alt köşe koordinatı
#4 fontu 5 boyutu rengi kalınlık 6 daha iyi gözükmesi için line komutunu kullan 
font=cv2.FONT_HERSHEY_COMPLEX

cv2.putText(img,'opencv',(10,400),font,4,(0,155,255),2,cv2.LINE_AA)


cv2.imshow("resim",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

