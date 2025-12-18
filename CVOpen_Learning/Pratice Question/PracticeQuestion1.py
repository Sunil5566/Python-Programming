import cv2

image_location = input("Enter the location of an image: ")

image = cv2.imread(image_location)

user_input = input(
    "Enter 'show' to see the image or 'save' to save the image: "
).lower()

if user_input == "show":
    if image is not None:
        cv2.imshow("Showing image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Image could not be loaded. Check the path.")

elif user_input == "save":
    if image is not None:
        file_name = input("Write the file name to save the image (with extension): ")
        cv2.imwrite(file_name, image)
        print("Image saved successfully.")
    else:
        print("Image could not be loaded. Cannot save.")

else:
    print("You have entered something else.")

