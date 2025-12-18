import cv2

image = cv2.imread("CVOpen_Learning/dog.jpeg")
                   
if image is not None:
    cv2.imshow("Showing image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

else:
    print("Image loaded successfully.")