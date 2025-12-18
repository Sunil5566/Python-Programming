import cv2

image = cv2.imread("Image_drawing_Functions\dog.jpeg")

if image is None:
    print("Opps! your image is not working.")

else:
    print("Image laoded successfully")

    pt1 = (50, 100)
    pt2 = (300, 100)
    color = (255, 0, 0)
    thickness = 4

    cv2.line(image, pt1, pt2, color, thickness)

    cv2.imshow("Line drawing", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
