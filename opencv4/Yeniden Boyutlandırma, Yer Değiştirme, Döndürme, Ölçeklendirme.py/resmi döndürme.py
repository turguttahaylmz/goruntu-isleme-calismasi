import cv2
import numpy as np 

img=cv2.imread("dron.jpg")

print(img.shape)

rows,cols=img.shape[:2]


#döndürme için opencv nin matrisi fonksiyonu var otomatik olarak döndürüyor 
rotation_matrix=cv2.getRotationMatrix2D((cols/2,rows/2),30,1)

img_rotation=cv2.warpAffine(img,rotation_matrix,(int(cols*1.2),int(rows*1.2)))

cv2.imshow("img",img)
cv2.imshow("img rotation",img_rotation)
cv2.waitKey()
cv2.destroyAllWindows()
                            