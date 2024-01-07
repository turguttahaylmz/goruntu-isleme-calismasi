#Name: matplotlib Version: 3.5.1
import matplotlib.pyplot as plt # Matplotlib'ı doğru bir şekilde içe aktarın
import cv2
#matplit kütüphanesi kullan  

#resim okuma imread okuma 
resim=cv2.imread("mf.jpg",0)#sağ tarafına 0 eklersen renksiz olur yani resim=cv2.imread("mf.jpg",0)  
#pencelrei adlandır diye başladık yanına bi parametre alırsa ona göre 
#oluşan pencere sabit kalıp ya da küçülp kalabilir 
cv2.namedWindow("resim ",cv2.WINDOW_AUTOSIZE)#window normal yapsak da resim büyüüyüp küçülebiliyor.

cv2.imshow("resim",resim)


#imshow resmi gösterme 
cv2.imshow("resim pencersi",resim)
plt.imshow(resim)
plt.show()


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