import cv2
image = cv2.imread("CVOpen_Learning/dog.jpeg") 
if image is not None: 
    success = cv2.imwrite("output.jpeg", image) 
    if success: 
        print("Image saved successfully as 'output.jpeg") 
        
    else: 
        print("Failed to save image.") 

else: 
    print("Image loaded successfully.")