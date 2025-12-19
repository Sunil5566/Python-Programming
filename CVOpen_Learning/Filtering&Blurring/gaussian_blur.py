import cv2

original_image = cv2.imread(r"C:\Users\subin\OneDrive\Desktop\Python_Project\CVOpen_Learning\Filtering&Blurring\images.jpeg")

blurred_iamge = cv2.GaussianBlur(original_image,(7,7), 0)

cv2.imshow("Original image", original_image)
cv2.imshow("Blurred image", blurred_iamge)

cv2.waitKey(0)
cv2.destroyAllWindows()