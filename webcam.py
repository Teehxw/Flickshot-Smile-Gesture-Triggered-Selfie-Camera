import cv2

stream = cv2.VideoCapture(0)

if not stream.isOpened():
    print("No Stream found")
    exit()

while True:
    result, frame = stream.read()
    if not result:
        print("No more stream")
        break
    
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