import os

#1. Learnt about the rename function
""" source = "C:/Users/delln/OneDrive/Desktop/projects/python-automation/File1.txt"
    dest = "C:/Users/delln/OneDrive/Desktop/projects/python-automation/File2.txt"
    os.rename(source,dest)"""

#2. 
data = "C:/Users/delln/OneDrive/Desktop/projects/python-automation/"
list1 = os.listdir(data)
counter = 0
for filename in list1:
    if filename.endswith(".txt"):
        counter+=1
        full_path = os.path.join(data,filename)
        new_full = "project-" + str(counter) + ".txt"
        #new_full = f"project-{counter}.txt"
        new_path = os.path.join(data,new_full)
        os.rename(full_path,new_path)