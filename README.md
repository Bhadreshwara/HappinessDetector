# HappinessDetector

What you need to build happiness detector:

Anaconda Navigator: https://docs.anaconda.com/anaconda/navigator/

OpenCV: https://opencv.org/

Haar Cascades (Data)

I’m using Spyder on Anaconda, but you could also use Jupyter NoteBook. Once you have everything, get on the IDE (code editor).

Haar Cascades - "Viola-Jones algorithm uses haar-like features to detect facial properties. The cascade is a series of filters that will apply one after the other to detect a face through its features."

# Importing OpenCV and Loading cascades

#Importing the Libraries

    import cv2 as cv

#Loading the Cascade

    face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
    smile_cascade = cv.CascadeClassifier('haarcascade_smile.xml')
   
 #  Defining the detection function on face, eyes, and smile
 
    def detect(gray, frame): # We create a function that takes as input the image in black and white (gray) and the original image (frame), and that will return the same image with the detector rectangles. 
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) # We apply the detectMultiScale method from the face cascade to locate one or several faces in the image.
    
    for (x, y, w, h) in faces: # For each detected face:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2) # We paint a rectangle around the face.
        roi_gray = gray[y:y+h, x:x+w] # We get the region of interest in the black and white image.
        roi_color = frame[y:y+h, x:x+w] # We get the region of interest in the colored image.
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3) # We apply the detectMultiScale method to locate one or several eyes in the image.
        for (ex, ey, ew, eh) in eyes: # For each detected eye:
            cv2.rectangle(roi_color,(ex, ey),(ex+ew, ey+eh), (0, 255, 0), 2) # We paint a rectangle around the eyes, but inside the referential of the face.
    return frame # We return the image with the detector rectangles.
    
  # Displaying the output on your webcam
  
    while True: # We repeat infinitely (until break):
      _, frame = video_capture.read() # We get the last frame.
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # We do some colour transformations.
      canvas = detect(gray, frame) # We get the output of our detect function.
      cv2.imshow('Video', canvas) # We display the outputs.
      if cv2.waitKey(1) & 0xFF == ord('q'): # If we type on the keyboard:
          break # We stop the loop.

     video_capture.release() # We turn the webcam off.
     cv2.destroyAllWindows() # We destroy all the windows inside which the images were displayed.
     
     
  # Output
  
      Try own your own and Have Fun!
