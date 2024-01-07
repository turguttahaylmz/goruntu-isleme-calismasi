import cv2

cam = cv2.VideoCapture(0)

#görüntü çekiyorum 
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#boş bir şablon oluştur ki içine aldığın görüntüyü yazalım 

out = cv2.VideoWriter("vs.avi", fourcc, 30.0, (640, 480))
#1.paremetre hangi görüntü içine koyacağız ,2.paremetre kodei,fps değeri,görüntünün boyutlanmasıdır


while cam.isOpened():# görüntüüyü açma 
    ret, frame = cam.read() #görüntü okuma 

    if not ret:#görüntü geliyor mu 
        print("kameradan görüntü alınamadı")
        break

    out.write(frame)# boş şablonun içine yazmalıyız

    
    cv2.imshow("kamera", frame)

    if cv2.waitKey(1) == ord("q"):
        print("videodan ayrıldınız")
        break

cam.release()#kamerayı kapat    
out.release()#boş şablonu da kapat 
cv2.destroyAllWindows()

