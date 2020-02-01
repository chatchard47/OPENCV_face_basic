import cv2
cap = cv2.VideoCapture("BLACKPINK - Kill This Love MV.mp4")
while (True):
        ret,frame = cap.read()
        #กรณีปรับแต่งให้เป็นภาพสีเทา
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #cv2.imshow('frame',gray)
        
        cv2.imshow('frame',frame)
        if (cv2.waitKey(1) & 0xFF == ord('q')):
                break
cap.release()
cv2.destroyAllWindows()
