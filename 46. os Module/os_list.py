import os

folders = os.listdir("Data")        # TO show List of under the Folder
print(folders)

# for folder in folders:
#     print(folder)

for folder in folders:
    print(folder, os.listdir(f"data/{folder}"))