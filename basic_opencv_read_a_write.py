import cv2
img = cv2.imread("cat2.jpg",0)
cv2.imshow('Show Result', img )
cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.imwrite('result.png', img )
