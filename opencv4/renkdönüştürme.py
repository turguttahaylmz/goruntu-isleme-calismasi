import cv2

#kamerayı tanıt videocapture= kamerayı yakala demek içine 0 girerseniz tanımlı olan pc nni kamerası girer başka kamera 1 2 3 olur 

can=cv2.VideoCapture(0)


 
while True:
    #rete true ya da faulse değerini döndürüyor kameradan görüntünün okunup okunamadığı hakkında bir değer 
    #frame ise resim çerçevesi veriyor
    ret,frame=can.read()
    #görüntüyü okuduktan sonra görüntüyü değiştirecem
    
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #ilk gireceğm parametre dönüştürmem gereken şeyler 
    #yani şimdi biz bunu istediğimiz gibi değiştirebilriz.
    

    if not ret:
        print("kameradan görüntü okunamıyo")
        break 

    cv2.imshow("kamera",frame)

   #basacağım tuş q ya eşit olursa kamear kapanır 
    key=cv2.waitKey(1)
    if key==ord("q"):
        print("görüntü sonlandırıldı.")
        break
#buraya kadar yazarsan kamera arka planda çalışır o yüzden 
can.release() #kamera kaptma işlemi 

#şimdi ise açtığımız pencereleri kapatma 
cv2.destroyAllWindows()

# aman dikkat bu kod çalıştımı durmuyor öğrenenen kadar bakma