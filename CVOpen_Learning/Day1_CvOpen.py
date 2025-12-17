import cv2


#..........................To Display Image in Window..........................
# image = cv2.imread("CVOpen_Learning/dog.jpeg")
                   
# if image is not None:
#     cv2.imshow("Showing image", image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
    

# else:
#     print("Image loaded successfully.")



image = cv2.imread("CVOpen_Learning/dog.jpeg")  
if image is not None:
    success = cv2.imwrite("output.jpeg", image)

    if success:
        print("Image saved successfully as 'output.jpeg")
    else:
        print("Failed to save image.")    
    

else:
    print("Image loaded successfully.")

