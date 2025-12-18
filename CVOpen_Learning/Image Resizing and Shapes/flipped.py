import cv2

image = cv2.imread("Phase2\dog.jpeg")

if image is None:
    print("Couldnot laod image.")
else:
    flipped_horizontal = cv2.flip(image, 1)
    flipped_verticle = cv2.flip(image, 0)
    flipped_both = cv2.flip(image, -1)

    cv2.imshow("Original", image)
    cv2.imshow("horizontal", flipped_horizontal)
    cv2.imshow("verticle", flipped_verticle)
    cv2.imshow("both", flipped_both)

    cv2.waitKey(0)
    cv2.destroyAllWindows()