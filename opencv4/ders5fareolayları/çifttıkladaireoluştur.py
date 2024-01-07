import cv2
import numpy as np
#içine 4 paremetre girer 1.si event,2.x,3.y 4 ve 5 de gelir 
def draw(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),50,(255,0,0),-1)
    


img=np.ones((512,512,3),np.uint8)#görüntü oluşturdum 

cv2.namedWindow("paint")#boş pencere oluşturdum 
#ilk girmemiz gereken pencerinin ismi 2.paremetre ise bir fonksiyon 
cv2.setMouseCallback('paint',draw)

cv2.imshow("paint",img)#cv2.imshow() fonksiyonu, iki argüman almalıdır: pencere adı ve görüntü matrisi.
while True:
    cv2.imshow("paint", img)
    key = cv2.waitKey(1)

    if key == ord("q"):
        break

cv2.destroyAllWindows()

#Daireyi çizdikten sonra cv2.imshow ile görüntüyü sürekli olarak güncellemeliyiz. Bu, her tıklamada dairelerin ekranda görünmesini sağlar.
#Sonsuz bir döngü (while True) kullanarak görüntüyü sürekli olarak güncellemeliyiz.
#cv2.waitKey(1) ile her döngüde bir tuşa basılıp basılmadığını kontrol ediyoruz. 'q' tuşuna basıldığında döngüyü sonlandırırız.