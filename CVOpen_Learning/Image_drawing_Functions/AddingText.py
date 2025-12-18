import cv2

image = cv2.imread("Image_drawing_Functions\dog.jpeg")

if image is None:
    print("Opps! your image is not working.")

else:
    print("Image laoded successfully")

    cv2.putText(image, "Hello Doggy", (50,100),
                cv2.FONT_HERSHEY_COMPLEX, 1.2, (0,255,255), 2)

    cv2.imshow("Adding Font here", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
