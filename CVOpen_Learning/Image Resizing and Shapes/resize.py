import cv2

image = cv2.imread("Phase2\dog.jpeg")

if image is None:
    print("Image is not found")

else:
    print("Image loaded.")

    resized = cv2.resize(image, (300,300))

    cv2.imshow("Original image", image)
    cv2.imshow("Resized Image", resized)

    cv2.imwrite("rezied_output.png", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()