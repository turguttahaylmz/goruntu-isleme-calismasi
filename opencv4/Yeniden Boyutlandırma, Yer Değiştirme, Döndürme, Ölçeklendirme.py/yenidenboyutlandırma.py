import cv2

img = cv2.imread("dron.jpg")

# İlk boyutlandırma işlemi
res = cv2.resize(img, (300, 300))

# İkinci boyutlandırma işlemi (yükseklik oranını değiştirerek)
res = cv2.resize(res, dsize=(0, 0), fx=1, fy=1.4,interpolation=cv2.INTER_CUBIC)#interpolation=cv2.INTER_CUBIC matris çarpımı için kullanılıyor. 

#dsize, yeniden boyutlandırılan resmin hedef boyutunu belirlemek için 
#kullanılan bir argümandır. Bu boyut, (genişlik, yükseklik) formatında bir tuple (demet) olarak belirtilir. 
# Ancak bu kullanımda, dsize yerine fx ve fy kullanıldı. fx ve fy, yeniden boyutlandırma oranını yatay ve dikey eksende belirler.

cv2.imshow("res", res)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
