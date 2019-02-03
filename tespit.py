import cv2
recognizer=cv2.face.LBPHFaceRecognizer_create()
recognizer.read("training/trainer.yml")
cascadePath="face.xml"
faceCascade=cv2.CascadeClassifier(cascadePath)
path="yuzveileri"
cam=cv2.VideoCapture()
while True:
    _,resim=cam.read()
    gri=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gri,scaleFactor=1.2,minNeighbors=5)
    for (x,y,w,h) in faces:
        tahminEdilenKisi,conf=recognizer.predict(gri[y:y+h,x:x+w])
        tahminEdilenKisi="yusuf korucu"