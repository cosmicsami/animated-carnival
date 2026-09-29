import cv2,numpy,os
dataset="peops"
peter="sami"
path=os.path.join(dataset,peter)
if not os.path.isdir(path):
    os.mkdir(path)
face_cascade=cv2.CascadeClassifier(r"images\haarcascade_frontalface_default.xml")
webcam=cv2.VideoCapture(0)
count=1
while count<=30:
    _,picter=webcam.read()
    greydout=cv2.cvtColor(picter,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(greydout,1.3,4)
    for face in faces:
        x,y,w,h=face
        cv2.rectangle(picter,(x,y),(x+w,y+h),[144,211,7],5)
        face=greydout[y:y+h,x:x+w]
        cv2.imwrite("%s/%s.png"%(path,count),face)
    count=count+1
        
    cv2.imshow("thisisaterribletitle",picter)
    key=cv2.waitKey(100)
    if key==27:
        break
    cv2.destroyAllWindows()
#this take a picture
