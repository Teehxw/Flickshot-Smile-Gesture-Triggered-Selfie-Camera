import cv2
import time
from face_detect import detect_faces, draw_faces, detect_smiles, draw_smiles

# TIMER
smile_timer_started = False
smile_start_time = None
countdown = 3
stream = cv2.VideoCapture(0)


# COOLDOWN TIMER 
cooldown_started = False
cooldown_start_time = None
cooldown = 5


if not stream.isOpened():
    print("No Stream found")
    exit()

# -***************************** MAIN LOOP *************************************
while True:
    smile_detected = False
    result, frame = stream.read()

    if not result:
        print("No more stream")
        break
    frame = cv2.flip(frame, 1)

    # Clean frame before rectangles are drawn
    clean_frame = frame.copy()

    # COOLDOWN CHECK
    if cooldown_started:
        cooldown_elapsed = time.time() - cooldown_start_time

        if cooldown_elapsed < cooldown:
            cv2.imshow("Webcam", frame)
            key = cv2.waitKey(1)

            if key == ord('q'):
                break

            continue

    else:
        cooldown_started = False
        cooldown_start_time = None


    # Call the functions from the face_detect file
    faces = detect_faces(frame)
    frame = draw_faces(frame, faces)

    for face in faces:
        x, y, w, h = face
        face_crop = frame[y:y+h, x:x+w]
        lower_face = face_crop[h//2:h, 0:w]
        smiles = detect_smiles(lower_face)
        frame = draw_smiles(frame, face, smiles)

        if smiles:
            smile_detected = True

    cv2.imshow('Face Detection', frame)

    # SMILE TIMER COUNTDOWN

    if smile_detected and not smile_timer_started:
        smile_timer_started = True
        smile_start_time = time.time()

    if smile_timer_started:
        elapsed_time = time.time() - smile_start_time
        remaining_time = countdown - elapsed_time

        # Draw the timer on the webcam 
        cv2.putText(
            frame, str(int(remaining_time) + 1),
            (50, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            5, 
            (0, 0, 255),
            6
        )
        
        if elapsed_time >= countdown:
            selfie_f = f"selfies/selfie_{int(time.time())}.jpg"
            cv2.imwrite(selfie_f, clean_frame)
            print("Selfie Successfully taken!")

            # Add a flash effect to indicate that a photo has been taken
            flash_frame = frame.copy()
            flash_frame[:] = (255, 255, 255)
            cv2.imshow("Webcam", flash_frame)
            cv2.waitKey(150)


            smile_timer_started = False
            smile_start_time = None

            # Start Cooldown
            cooldown_started = True
            cooldown_start_time = time.time()

    
    # Taking selfies
    cv2.imshow("Webcam", frame)
    key = cv2.waitKey(1)

    if key == ord('s'):
        cv2.imwrite('selfies/image.jpg', clean_frame)
        print("screenshot saved")
         
    elif key == ord('q'):
        print("Stream closed")
        break

stream.release()
cv2.destroyAllWindows()