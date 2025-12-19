import cv2
import numpy as np

original_image = cv2.imread(r"C:\Users\subin\OneDrive\Desktop\Python_Project\CVOpen_Learning\Filtering&Blurring\images.jpeg")

sharpen_kernal = np.array([
[0, -1, 0],
[-1, 5, -1],
[0, -1, 0]
])

sharpened_image = cv2.filter2D(original_image, -1, sharpen_kernal)

cv2.imshow("Original image", original_image)
cv2.imshow("Sharpened image", sharpened_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
