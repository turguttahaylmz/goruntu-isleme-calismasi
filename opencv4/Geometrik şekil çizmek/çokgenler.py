
import cv2
import numpy as np 
#sıfırlardan oluşan bir matris olursa siyah olacak 
img=np.zeros((512,512,3),np.uint8)#3 boyutlu olur
#nupydan matris oluştur 
pts=np.array([[20,30],[100,120],[255,255],[10,400]],np.int32)
pts2=pts.reshape(-1,1,2)#reshape yeniden şekillendirmek demektir
cv2.polylines(img,[pts],True,(255,255,255),3)#true olursa çokgen oluşur



cv2.imshow("resim",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

