import os
# specify the directory path
dir_path = "E:\Wee-A-Boo\Tales of Demons and Gods\S1"



print(os.listdir(dir_path))



# # loop through all files in the directory
# for filename in os.listdir(dir_path):

#     # check if the file is a text file
#     if filename.endswith(".txt") or filename.endswith(".mp4"):

#         # construct the old file path
#         old_file_path = os.path.join(dir_path, filename)

#         # construct the new file name
#         new_file_name = f"new_{filename}"

#         # construct the new file path
#         new_file_path = os.path.join(dir_path, new_file_name)