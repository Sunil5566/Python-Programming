import os
import cv2
import csv
from datetime import datetime

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

face_cascade = cv2.CascadeClassifier(r"CVOpen_Learning\Project_Smart Attendance System\haarcascade_frontalface_default.xml")

if face_cascade.empty():
    print("No Cascade is there in file..Check Again.")
    exit()

attendance_file = "attendance.csv"

if not os.path.exists(attendance_file):
    with open(attendance_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Date", "Time"])

person_name = input("Enter Person Full Name: ").strip()

def mark_attendance(name):
    today_date = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H:%M:%S")

    with open(attendance_file, "r+", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

        for row in rows:
            if row[0] == name and row[1] == today_date:
                return False  # already marked

        writer = csv.writer(file)
        writer.writerow([name, today_date, current_time])
        print(f"Attendance marked for {name}")
        return True  # new attendance

# Main loop
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
    
        # Call attendance
        new_marked = mark_attendance(person_name)
    
        # Show status text
        status_text = "New Attendance Marked" if new_marked else "Already Marked"
        cv2.putText(
            frame,
            status_text,
            (x, y-10),
            cv2.FONT_HERSHEY_COMPLEX,
            0.7,
            (0, 255, 0),
            2
        )    
    
    cv2.imshow("Student Attendance - Face Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
