import cv2

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Camera is not opened yet.")
    exit()

previous_frame = None 
while True:
    success, frame = camera.read()
    if not success:
        print("Failed to read frame.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if previous_frame is not None:
        
        pass

    previous_frame = gray.copy()

    cv2.imshow("Original Frame", frame)
    cv2.imshow("Gray Frame", gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
