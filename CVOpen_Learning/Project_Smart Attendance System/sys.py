import cv2

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

face_cascade = cv2.CascadeClassifier(
    r"CVOpen_Learning\Project_Smart Attendance System\haarcascade_frontalface_default.xml"
)

if face_cascade.empty():
    print("Error loading cascade file")
    exit()

while True:
    ret, frame = camera.read()

    if not ret:
        print("Could not read frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(60, 60)
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

    cv2.imshow("Smart Attendance - Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
