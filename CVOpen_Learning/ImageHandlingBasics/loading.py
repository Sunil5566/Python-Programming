import cv2

image = cv2.imread("CVOpen_Learning/dog.jpeg")

if image is None:
    print("Error: Image not found.")
else:
    print("Image loaded successfully.")    