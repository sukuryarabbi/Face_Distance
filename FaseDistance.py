import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector

capture = cv2.VideoCapture(0)

detector = FaceMeshDetector(maxFaces=1)

while True :

    ret,frame = capture.read()

    frame,faces = detector.findFaceMesh(frame , draw=False )

    if faces :

        face = faces[0]
        pointLeft = face[145]
        pointRight = face[374]


        #Burada gözlerimin konumu buldurttum ardından iki göz arasında ki mesafeyi ölçtüm(Formül için gerekli !!!)
        cv2.circle(frame , pointLeft , 5 , (0,255,0) , 2)
        cv2.circle(frame , pointRight , 5 , (0,255,0) , 2)
        cv2.line(frame , pointLeft , pointRight , (0,200,0) , 3)

        w , _ =detector.findDistance(pointLeft , pointRight)
        
        #w = kameraya göre mesafe(width), f = kameranın uzunluğu(frame) , W = bizim genişliğimiz , d = mesafe 
        #Bu alttaki formüller analitik geometri bilgisi ile geliyor :D

        W=6.3
        #d=50
        #f=(w*d)/W

        f=630
        d=(W*f)/w

        cvzone.putTextRect(frame , f"Mesafe : {int(d)} cm " , (face[10][0] , face[10][1]), scale=3)

    cv2.imshow("Kamera" , frame)

    kInp = cv2.waitKey(1)

    if(kInp == ord("q")) :

        break 

cv2.destroyAllWindows()
capture.release()