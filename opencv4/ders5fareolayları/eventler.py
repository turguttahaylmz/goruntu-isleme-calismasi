import cv2
import numpy as np
#içine 4 paremetre girer 1.si event,2.x,3.y 4 ve 5 de gelir 
def draw(event,x,y,flag,param):
    print(x,y)
    pass 


img=np.ones((512,512,3),np.uint8)#görüntü oluşturdum 




cv2.namedWindow("paint")#boş pencere oluşturdum 

#ilk girmemiz gereken pencerinin ismi 2.paremetre ise bir fonksiyon 
cv2.setMouseCallback('paint',draw)

cv2.imshow("paint",img)#cv2.imshow() fonksiyonu, iki argüman almalıdır: pencere adı ve görüntü matrisi.
key=cv2.waitKey(0)
if key==ord("q"):
    print("görüntü sonlandırıldı.")
    
cv2.destroyAllWindows()