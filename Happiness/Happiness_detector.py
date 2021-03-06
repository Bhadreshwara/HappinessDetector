#Importing the Libraries
import cv2 as cv




#Loading the Cascade
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv.CascadeClassifier('haarcascade_smile.xml')
mouth_cascade = cv.CascadeClassifier('Mouth.xml')
nose_cascade = cv.CascadeClassifier('Nariz.xml')
eye_withglasses_cascade = cv.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

#Defining a function that will do the detections
def detect(gray, frame):
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        fx=x
        fy=y
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        cv.putText(roi_color,"Face",(fx, fy), cv.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 1)
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 22)
        for (ex, ey, ew, eh) in eyes:
            cv.rectangle(roi_color,(ex, ey),(ex+ew, ey+eh), (0, 255, 0), 2)
            cv.putText(roi_color,"eyes",(ex, ey), cv.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 0), 1)     
        eyes_withgl = eye_withglasses_cascade.detectMultiScale(roi_gray, 1.1, 22)
        for (ex, ey, ew, eh) in eyes:
            cv.rectangle(roi_color,(ex, ey),(ex+ew, ey+eh), (0, 255, 0), 2)
            cv.putText(roi_color,"eyes",(ex, ey), cv.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 0), 1)
        smile = smile_cascade.detectMultiScale(roi_gray, 1.8, 25)
        for (sx, sy, sw, sh) in smile:
            cv.rectangle(roi_color,(sx, sy),(sx+sw, sy+sh), (255, 0, 255), 2)
            cv.putText(roi_color,"smile",(sx, sy), cv.FONT_HERSHEY_SIMPLEX, 0.55, (255, 0, 255), 1)
        nose = nose_cascade.detectMultiScale(roi_gray, 1.8, 20)
        for (nx, ny, nw, nh) in nose:
            cv.rectangle(roi_color,(nx, ny),(nx+nw, ny+nh), (255, 0, 0), 2)
            cv.putText(roi_color,"nose",(nx, ny), cv.FONT_HERSHEY_SIMPLEX, 0.55, (255, 0, 0), 1)
    return frame

#Doing some Face Recognition with the Webcame
cap = cv.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    _, frame = cap.read()
    
    #Converting into Gray
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)  
    
    canvas = detect(gray, frame)    
    
    cv.imshow('Video', canvas)
    
    crop = frame[100:300, 40:240]
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
    
    

    
        
        
        