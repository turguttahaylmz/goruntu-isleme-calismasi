import cv2 


#kameratanımlıyoruz içine gelen ise açıcağımvideonun ismi olmalı
cam=cv2.VideoCapture("video.mp4")


while cam.isOpened():
    ret,frame=cam.read()

    if not ret:
        print("kameradan görüntü okunamıyor")
        break 

    cv2.imshow("förüntü",frame)
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#resmi gri yaptık 
    
    key=cv2.waitKey(1)
    if key==ord("q"):
        print("görüntü sonlandırıldı.")
        break

cam.release()
cv2.destroyAllWindows()


