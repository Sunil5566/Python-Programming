import cv2

img = cv2.imread(r"C:\Users\subin\OneDrive\Desktop\Python_Project\CVOpen_Learning\Edge Detection in Opencv\man.jpeg", cv2.IMREAD_GRAYSCALE)

ret, thresh_img = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY)

cv2.imshow("Original image", img)
cv2.imshow("Threshold Image", thresh_img)

cv2.waitKey(0)
cv2.destroyAllWindows()