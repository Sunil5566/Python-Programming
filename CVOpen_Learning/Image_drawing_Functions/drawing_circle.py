import cv2

image = cv2.imread("Image_drawing_Functions\dog.jpeg")

if image is None:
    print("Opps! your image is not working.")

else:
    print("Image laoded successfully")

    cv2.circle(image, (100,100), 50, (255,0,0), -1)

    cv2.imshow("Circle Drawing drawing", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
