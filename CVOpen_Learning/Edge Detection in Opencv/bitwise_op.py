"""
Docstring for CVOpen_Learning.Edge Detection in Opencv.bitwise_op
1- cv2.bitwise_or(img1, img2)
2- cv2.bitwise_and(img1, img2)
3- cv2.bitwise_not(img1)

* img 1 and img 2 height and width should be equal
* use only black and white
* 

"""
import cv2
import numpy as np

img1 = np.zeros((300,300), dtype = "uint8")
img2 = np.zeros((300,300), dtype = "uint8")

cv2.circle(img1, (100,100), 100, 255, -1)
cv2.rectangle(img2, (150,150), (250,250), 255, -1)


bitwise_and = cv2.bitwise_and(img1, img2)
bitwise_or = cv2.bitwise_or(img1, img2)
bitwise_not = cv2.bitwise_not(img1)

cv2.imshow("Circle", img1)
cv2.imshow("rectangle", img2)
cv2.imshow("Bitwise AND", bitwise_and)
cv2.imshow("Bitwise OR", bitwise_or)
cv2.imshow("Bitwise NOT", bitwise_not)

cv2.waitKey(0)
cv2.destroyAllWindows()
