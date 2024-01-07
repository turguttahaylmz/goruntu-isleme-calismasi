import cv2

img1=cv2.imread("siha.png")
img2=cv2.imread("iha.jpg")

x,y,z=img1.shape
roi=img2[0:x,0:y]#resmi bi kırpıyoruz 
#önce bi resmimizi gri tona çevirelim 
img1_gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
#vgr griye döndürürüz

ret,mask=cv2.threshold(img1_gray,10,255,cv2.THRESH_BINARY)
#0 ları 1 1 leri 0 yapacaz

mask_inv=cv2.bitwise_not(mask)

img1_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)

img2_fg=cv2.bitwise_and(img1,img1,mask=mask)

toplam=cv2.add(img1_bg,img2_fg)

img2[0:x,0:y]=toplam
#kırpılan yerde bitsel olrak bi çarpma yapacağız ki görüntünün eklemek istedğim yerler 0 olsun geri kalan aynı kalsın 

cv2.namedWindow("resim",cv2.WINDOW_NORMAL)
cv2.imshow("resim",img2)
cv2.imshow("resim2",toplam)
cv2.waitKey(0)
cv2.destroyAllWindows()