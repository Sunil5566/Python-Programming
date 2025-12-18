import cv2

image = cv2.imread("Image_drawing_Functions\dog.jpeg")

if image is None:
    print("Opps! your image is not working.")

else:
    print("Image laoded successfully")

    pt1 = (50, 150)
    pt2 = (200, 100)
    color = (255, 0, 0)
    thickness = -1

    cv2.rectangle(image, pt1, pt2, color, thickness)

    cv2.imshow("Rectangle drawing", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
