import cv2
import numpy as np

with open("fileHandling.txt", "w") as file:
    file.write("Drawing started...\n")

file_location = input("Enter image file path (or press Enter to create blank canvas): ")

if file_location:
    image = cv2.imread(file_location)
    if image is None:
        print("Could not load image, creating blank canvas instead.")
        image = np.zeros((500, 500, 3), dtype=np.uint8)
else:
    image = np.zeros((500, 500, 3), dtype=np.uint8)

user_desire = input(
    "What do you want to do? Draw circle(c), Draw rectangle(r), Draw line(l), Put text(t): "
).lower()

if user_desire == "c":
    cv2.circle(image, (250, 250), 100, (255, 0, 0), -1)
elif user_desire == "r":
    cv2.rectangle(image, (100, 100), (400, 300), (0, 255, 0), -1)
elif user_desire == "l":
    cv2.line(image, (50, 50), (450, 450), (0, 255, 255), 5)
elif user_desire == "t":
    text_to_write = input("Enter the text to put on image: ")
    cv2.putText(image, text_to_write, (50, 250), cv2.FONT_HERSHEY_COMPLEX, 1.5, (0, 255, 0), 3)
else:
    print("Invalid choice!")

cv2.imshow("Result", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

save_choice = input("Do you want to save the image? (y/n): ").lower()
if save_choice == "y":
    save_path = input("Enter file name to save (example: output.jpg): ")
    cv2.imwrite(save_path, image)
    print(f"Image saved as {save_path}")
    with open("fileHandling.txt", "a") as file:
        file.write(f"Image saved as {save_path}\n")
else:
    print("Image not saved.")
    with open("fileHandling.txt", "a") as file:
        file.write("Image not saved.\n")
