import cv2
import numpy as np

def draw(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 50, (0, 0, 255), -1)

img = np.ones((512, 512, 3), np.uint8)  

cv2.namedWindow("paint")
cv2.setMouseCallback('paint', draw)

while True:
    cv2.imshow("paint", img)
    key = cv2.waitKey(1)

    if key == ord("q"):
        break

cv2.destroyAllWindows()
