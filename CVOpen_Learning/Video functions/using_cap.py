import cv2
# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read() # return true or false  ,frame = image

#     if not ret:
#         print("Couldnot read frame")
#         break

#     cv2.imshow("Webcam feed", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         print("Quiting")
#         break
# cap.release()
# cv2.destroyAllWindows()


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Couldnot read frame.")
        break
    cv2.imshow("webcam feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
     print("Quiting")
     break

cap.release()
cv2.destroyAllWindows()

