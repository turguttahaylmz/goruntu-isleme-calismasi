import cv2
import matplotlib.pyplot as plt

res=cv2.imread("resim.jpg")

kırp=res[500:800,500:800]  #resmi kırpıyoruz 
#önceki resmi silmeyeyim iksini beraber gösterelim 
res[(0,0,3),(61,0,3)]=kırp 

plt.subplot(121)
plt.imshow(res,"gray")
plt.subplot(122)
plt.imshow(kırp)
plt.show()
