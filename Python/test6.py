import os

folder_path = input("Enter the folder path: ")

with open("file_names.txt", "w") as file:
    for f in os.listdir(folder_path):
        file.write(os.path.basename(f) + "\n")