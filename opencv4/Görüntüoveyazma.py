import cv2


#resim okuma imread okuma 
resim=cv2.imread("mf.jpg",0)#sağ tarafına 0 eklersen renksiz olur yani resim=cv2.imread("mf.jpg",0)  

#imshow resmi gösterme 
cv2.imshow("resim pencersi",resim)

#waitkey bekleme tuşu o yüzden içen 0 yazarım çünkü herhangi bi tuşa basana kadar beklesin
k=cv2.waitKey(0)

#hexadecimal characters e göre tuşların sayı karşılığıu var mesela 27 ESC DİR


if k==27:
    print("esc tuşuna basıldı")
elif k==ord("q"):
    print("q tuşuna basıldı,resim kaydedildi")
    cv2.imwrite("mfgri.jpg",resim)

#.destroyAllWindows tüm pencereleri kapatmak için 
cv2.destroyAllWindows() 
