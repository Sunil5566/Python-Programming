import cv2

original_image = cv2.imread(r"C:\Users\subin\OneDrive\Desktop\Python_Project\CVOpen_Learning\Filtering&Blurring\images.jpeg")
blurred_image = cv2.medianBlur(original_image, 11)

cv2.imshow("Original iamge", original_image)
cv2.imshow("blurred image", blurred_image)

cv2.waitKey(0)
cv2.destroyAllWindows()