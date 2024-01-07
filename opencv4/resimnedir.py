import cv2
import numpy as np

sıfır=np.zeros([300,300])
bir=np.ones([300,300])

cv2.namedWindow("sıfır",cv2.WINDOW_NORMAL)
cv2.namedWindow("bır",cv2.WINDOW_NORMAL)

cv2.imshow("sıfır",sıfır)
cv2.imshow("bir",bir)

cv2.waitKey(0)

cv2.destroyAllWindows()


# yani her resim matrisdi


