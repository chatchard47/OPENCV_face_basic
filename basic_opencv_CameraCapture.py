import cv2
cap = cv2.VideoCapture(0)
while (True):
        ret,freme = cap.read()
        cv2.imshow('March',freme)
        if (cv2.waitKey(1)& 0xFF == ord('q')):
         break
cap.release()
cv2.destroyWindows()
