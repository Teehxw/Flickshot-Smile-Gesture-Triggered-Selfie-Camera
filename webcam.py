import cv2
import os

stream = cv2.VideoCapture(0)

if not stream.isOpened():
    print("No Stream found")
    exit()

face_cascade = cv2.CascadeClassifier('/Users/taahaar/Documents/GitHub/Flickshot-Smile-Gesture-Triggered-Selfie-Camera/haar_cascades/gpreda__haar-cascades-for-face-detection/haarcascade_frontalface_alt2.xml')

while True:
    result, frame = stream.read()
    if not result:
        print("No more stream")
        break
    
    
    gray_face = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face = face_cascade.detectMultiScale(gray_face, scaleFactor = 1.1, minNeighbors=5)

    for (x,y,w,h) in face:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Face Detection', frame)
    
    # Taking selfies
    cv2.imshow("Webcam", frame)
    key = cv2.waitKey(1)
    if key == ord('s'):
        cv2.imwrite('selfies/image.jpg', frame)
        print("screenshot saved")
    elif key == ord('q'):
        print("Stream closed")
        break

stream.release()
cv2.destroyAllWindows()