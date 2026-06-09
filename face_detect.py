import cv2

# CASCADES
cascade = cv2.CascadeClassifier('/Users/taahaar/Documents/GitHub/Flickshot-Smile-Gesture-Triggered-Selfie-Camera/haar_cascades/gpreda__haar-cascades-for-face-detection/haarcascade_frontalface_alt2.xml')
smile_cascade = cv2.CascadeClassifier('/Users/taahaar/Documents/GitHub/Flickshot-Smile-Gesture-Triggered-Selfie-Camera/haar_cascades/gpreda__haar-cascades-for-face-detection/haarcascade_smile.xml')

### ---------------FUNCTIONS --------------------
def detect_faces(frame, scale_factor = 1.1, min_neighbors = 5, min_size = (80,80)):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray, scaleFactor=scale_factor, minNeighbors= min_neighbors, minSize=min_size)
    
    return list(faces)

def crop_faces(frame, faces):
    # make an empty list for thte cropped faces from the webcam
    cropped_faces = []

    for (x,y,w,h) in faces:
        crop_face = frame[y:y+h, x:x+w]
        cropped_faces.append(crop_face)

    return cropped_faces

def draw_faces(frame, faces):
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

    return frame

##DETECT SMILES within the FACE DETECTED
def detect_smiles(face_frame, scale_factor = 1.8, min_neighbors = 35, min_size = (25, 25)):
    gray = cv2.cvtColor(face_frame, cv2.COLOR_BGR2GRAY)

    smiles = smile_cascade.detectMultiScale(
        gray,
        scaleFactor=scale_factor,
        minNeighbors= min_neighbors,
        minSize=min_size
    )

    return list(smiles)

def draw_smiles(frame, face, smiles):
    x,y,w,h = face

    # within the detected face 
    for (sx, sy, sw, sh) in smiles:
        cv2.rectangle(frame, (x+sx, y+ h//2 + sy), 
            (x + sx + sw, y + h//2 + sy + sh),
            (255, 0, 0),
            2
        )

    return frame




