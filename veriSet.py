import cv2
cam=cv2.VideoCapture(0)
detector=cv2.CascadeClassifier('face.xml')
i=0
offset=50
kisi_id=input("ID bilgisi giriniz")
while True:
    _, resim=cam.read()
    gri=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
    faces=detector.detectMultiScale(gri,scaleFactor=1.2,minNeighbors=5,minSize=(100,100),flags=cv2.CASCADE_SCALE_IMAGE)
    for(x,y,w,h) in faces:
        i=i+1
        cv2.imwrite("yuzverileri/face-"+kisi_id+"."+str(i)+".jpg",gri[y-offset:y+h+offset,x-offset:x+w+offset])
        cv2.rectangle(resim,(x-offset,y-offset),(x+w+offset,y+h+offset),(0,0,255),2)
        cv2.waitKey(100)
    if i>20:
        cam.release()
        cv2.destroyAllWindows()
        break
