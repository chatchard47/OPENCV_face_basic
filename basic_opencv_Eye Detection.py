import cv2
#opencv/data/haarcascades/
#https://github.com/opencv/opencv/tree/master/data/haarcascades
faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eyeCascade=cv2.CascadeClassifier("haarcascade_eye.xml")

def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text):
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        features=classifier.detectMultiScale(gray,scaleFactor,minNeighbors)
        coords=[]
                #การวาดรูปภาพบนใบหน้า
        for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),color,2)#วาดสี่เหลี่ยมผืนผ้าบนหน้า
                cv2.putText(img,text,(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.8,color,2)
                coords=[x,y,w,h]
        return img ,coords
        
def detect(img,faceCascade,eyeCascade): 
        img,coords =draw_boundary(img,faceCascade,1.1,10,(0,0,255),"ME")
        img,coords =draw_boundary(img,eyeCascade,1.1,12,(255,0,0),"eye")

        return img


cap = cv2.VideoCapture(0)
while (True):
        ret,frame = cap.read()
        frame=detect(frame,faceCascade)
        cv2.imshow('frame',frame)
        if(cv2.waitKey(1) & 0xFF== ord('q')):
            break
cap.release()
cv2.destroyAllWindows()


