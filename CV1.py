import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#face_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

font = cv2.FONT_HERSHEY_COMPLEX

while True:
    # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    # Draw the rectangle around each face
    cv2.rectangle(img, (350, 250), (450, 350), (0, 0, 0), 2)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.rectangle(img, (x+round(w/2)-5, y+round(h/3)-5), (x+round(w/2)+5, y+round(h/3)+5), (0,0,255), 1)
        cv2.putText(img,'x=' + str(x) + ' y=' + str(y),(x,y),font,0.5,(255,255,255),2)
        if x+round(w/2)>350 and x+round(w/2)<450 and y+round(h/3)>250 and y+round(h/3)<350:
            cv2.rectangle(img, (350, 250), (450, 350), (0, 0, 255), 3)
    # Display
    cv2.imshow('img', img) 
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
# Release the VideoCapture object
cap.release()
