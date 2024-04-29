import os

# file extensions to check
files_extensions = [".mp4", ".mkv"]

# file directory
dir_path = ""

def directory():
    global dir_path
    
    print("List of modes :")
    print("1 to use current directory")
    print("2 to use user input directory")
    print("3 to add file extensions to check")
    mode = input("Choose Mode : ")
    if mode == "1":  
        # use current directory
        dir_path = os.getcwd()
        return dir_path
    elif mode == "2":
        # user inputed directory
        dir_path = input("Copy and Paste you directory here : ")
        return dir_path
    elif mode == "3":
        # add more extensions to check
        print(files_extensions)
        more_ext = str(input("Input extensions here (example : .mp3) : "))
        files_extensions.append(more_ext)
        print(more_ext, ' has been added')
        directory()
    else:
        print("wrong input!\n")
        directory()

def get_files(dir_path):
    # get file list in a directory
    files_names = os.listdir(dir_path)
    return files_names

# # checking which to slice
# for x in range(0, len(files_names[1])):
# 	print(files_names[1][x], " | ", x)

# #checking for every files and every file extensions
# for filename in files_names:
#     # check if the file is something
#     for file_ext in range(0, len(files_extensions)):
#         if filename.endswith(files_extensions[file_ext]):
#             old_file_path = os.path.join(dir_path, filename)
#             filename_new = filename[11:len(filename)]
#             new_file_path = os.path.join(dir_path, filename_new)
#             os.rename(old_file_path, new_file_path)

directory()
print(dir_path)
