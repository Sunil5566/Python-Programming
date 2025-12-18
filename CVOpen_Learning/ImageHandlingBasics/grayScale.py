# import cv2

# image = cv2.imread("CVOpen_Learning/dog.jpeg")

# if image is not None:
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     cv2.imshow("GrayScale Image", gray)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# else:
#      print("Couldnot load the image.")   


import cv2

image = cv2.imread("CVOpen_Learning/dog.jpeg")

#Converting colorful image into gray image

if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("GrayScale Image", gray)
    

