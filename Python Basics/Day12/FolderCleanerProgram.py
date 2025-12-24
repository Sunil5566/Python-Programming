import csv
import os

list = []
folder_path = input("Enter your folder path: ")
Image = os.path.join(folder_path, "Image")
Video = os.path.join(folder_path, "Videos")
Documents = os.path.join(folder_path, "Documents")
Others = os.path.join(folder_path, "Others")


folders = [folder_path, Image, Video, Documents, Others]

for fol in folders:
    if not os.path.exists(fol):
        os.mkdir(fol)

# To check if any file is in inside folder or not

file = []
list1 = os.listdir(folder_path)

for items in list1:
    full_path = os.path.join(folder_path, items)

    if os.path.isfile(full_path):
        file.append(items)

if len(file) == 0:
    print("There is not any file")

else:
    print(file)

for f in file:
    name, extension = os.path.splitext(f)

    image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"]
    video_extensions = [
        ".mp4",
        ".mkv",
        ".avi",
        ".mov",
        ".wmv",
        ".flv",
        ".webm",
        ".mpeg",
        ".3gp",
    ]

    document_extensions = [
        ".txt",
        ".pdf",
        ".doc",
        ".docx",
        ".xls",
        ".xlsx",
        ".ppt",
        ".pptx",
        ".csv",
        ".json",
        ".xml",
        ".html",
        ".css",
        ".js",
        ".py",
        ".java",
        ".c",
        ".cpp",
        ".sql",
        ".md",
    ]

    ext = extension.lower()

    if ext in image_extensions:
        target_folder = Image
    elif ext in video_extensions:
        target_folder = Video
    elif ext in document_extensions:
        target_folder = Documents
    else:
        target_folder = Others          


    source_path = os.path.join(folder_path,f)
    destination_path = os.path.join(target_folder,f)

    if os.path.exists(destination_path):
        counter = 1
        new_file = f"{name}_{counter}{extension}"

        while os.path.exists(os.path.join(target_folder,new_file)):
            counter += 1
            new_file = f"{name}_{counter}{extension}"

        destination_path = os.path.join(target_folder,new_file)

    os.rename(source_path, destination_path)               
