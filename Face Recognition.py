import cv2
facedetection = cv2.CascadeClassifiers('haarcascade_frontalface_alt.xml')
img=cv2.imread('https://images.app.goo.gl/oHwuamWbB1ZMfsiA7')

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face= facedetection.detectMultiScale(gray,1,1,4)

for (x,y,w,h) in face:
  cv2.rectangle(img,(x,y),(x+y,w+h),(0,255,0),1)

cv2.imshow(r,img)
cv2.waitKey()
