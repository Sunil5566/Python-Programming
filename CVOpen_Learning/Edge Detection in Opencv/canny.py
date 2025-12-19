import cv2

img = cv2.imread(r"C:\Users\subin\OneDrive\Desktop\Python_Project\CVOpen_Learning\Edge Detection in Opencv\flower.webp", cv2.IMREAD_GRAYSCALE)

edges = cv2.Canny(img, 50, 150)

cv2.imshow("Original image", img)
cv2.imshow("Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()