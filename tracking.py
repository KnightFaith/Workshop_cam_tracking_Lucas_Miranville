import numpy as np
import cv2

#img = cv2.imread('./akatsuki.png', 0)
#cv2.imshow('image viewer', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

img = cv2.imread('./akatsuki.png', 0)
while True:
    cv2.imshow('image viewer', img)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()