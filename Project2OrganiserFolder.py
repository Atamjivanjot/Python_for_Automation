#1. open the folder and list all the files
#2. loop through the list and check the extension
#3. put them in their respective folders

import os
import shutil

path = "practice-downloads"

os.makedirs(f"{path}/Images", exist_ok=True)
os.makedirs(f"{path}/PDFs", exist_ok=True)
os.makedirs(f"{path}/Docs", exist_ok=True)
os.makedirs(f"{path}/Others", exist_ok=True)

for file in os.listdir(path):

    full_path = os.path.join(path, file)

    if os.path.isfile(full_path):

        if file.endswith((".jpg", ".png", ".jpeg")):
            shutil.move(full_path, os.path.join(path, "Images", file))

        elif file.endswith(".pdf"):
            shutil.move(full_path, os.path.join(path, "PDFs", file))

        elif file.endswith((".txt", ".docx")):
            shutil.move(full_path, os.path.join(path, "Docs", file))

        else:
            shutil.move(full_path, os.path.join(path, "Others", file))

print("Files organized successfully!")