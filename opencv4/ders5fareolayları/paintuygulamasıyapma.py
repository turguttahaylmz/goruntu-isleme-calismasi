#fare hareket etme 
#farenin sol tuşuna bastığında kalkması lazım 
#sol tuşuna bastığında çizmesi lazım 
import cv2
import numpy as np

cizim=False #burada bunu yaptık çünkü elimizi kaldırdığımız vakit çizim dursun 
mod=False
xi,yi=-1,-1

#içine 4 paremetre girer 1.si event,2.x,3.y 4 ve 5 de gelir 
def draw(event,x,y,flags,param):
    global cizim,xi,yi,mod #global olması lazım ki değişebilsin 
   
    if event==cv2.EVENT_LBUTTONDOWN:#sol buton lazım 
        xi,yi=x,y
        cizim=True
    elif event==cv2.EVENT_MOUSEMOVE:#maousum hareketlerini görmem lazım 
        if cizim==True:
            if mod:
                cv2.circle(img,(x,y),10,(100,50,0),-2)
            else:
              cv2.rectangle(img,(xi,yi),(x,y),(0,0,255),3)
        else:
            pass

    elif event==cv2.EVENT_LBUTTONUP:#sol buton lazım 
        cizim=False 

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
    if key == ord("m"):
        mod=not mod 
#m tuşuna basyım dikdörtgen m tuşuna basayım başka şekil çizeyim 


cv2.destroyAllWindows()

#Daireyi çizdikten sonra cv2.imshow ile görüntüyü sürekli olarak güncellemeliyiz. Bu, her tıklamada dairelerin ekranda görünmesini sağlar.
#Sonsuz bir döngü (while True) kullanarak görüntüyü sürekli olarak güncellemeliyiz.
#cv2.waitKey(1) ile her döngüde bir tuşa basılıp basılmadığını kontrol ediyoruz. 'q' tuşuna basıldığında döngüyü sonlandırırız.