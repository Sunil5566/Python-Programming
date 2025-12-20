import cv2

face_cascade = cv2.CascadeClassifier(
    r"CVOpen_Learning\Face and Object Detection\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(
    r"CVOpen_Learning\Face and Object Detection\haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier(
    r"CVOpen_Learning\Face and Object Detection\haarcascade_smile.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # ✅ check frame
    if not ret:
        print("Could not read frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        # draw face rectangle
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)
        if len(eyes) > 0:
            cv2.putText(frame, "Eyes detected",
                        (x, y-30),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6, (0, 0, 255), 2)

        smile = smile_cascade.detectMultiScale(roi_gray, 1.7, 20)
        if len(smile) > 0:
            cv2.putText(frame, "Smiling",
                        (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6, (0, 0, 255), 2)

    cv2.imshow("Smart face detector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
