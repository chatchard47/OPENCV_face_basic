import cv2
img = cv2.imread("cat.jpg",1)

img = cv2.line(img,(10,50),(200,300),(0,0,255),5)
img = cv2.arrowedLine(img,(0,0),(400,400),(255,0,0),5)
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),5)

img = cv2.circle(img,(447,250),70,(0,255,0),-1)
img = cv2.circle(img,(447,550),70,(0,255,0),1)
img = cv2.circle(img,(447,700),70,(0,255,0),10)

img = cv2.putText(img,"opencv-cat",(600,400),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
cv2.imshow('Show Result', img )
cv2.waitKey(0)

cv2.destroyAllWindows()


