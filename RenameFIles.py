# TO DO
# Check the files to match extensions only DONE
# Add an extra file to store extensions
# Mode 1 which use current directory is still broken DONE
# add confirmation before renaming
# add history system
# add custom names instead of just slicing
# add fail safe to guard from files that has different character length ex : myfile1, my file03, my file11

#How to build :
# pyinstaller -F RenameFiles.py

import os
import time

# file extensions to check
files_extensions = [".mp4", ".mkv"]

# file directory
dir = True

cont = True

# first
def directory():
    global dir_path

    print("Current extensions to check : ")
    print(files_extensions)
    print("List of modes :")
    print("1 to use current directory")
    print("2 to use user input directory")
    print("3 to add file extensions to check")
    print("4 to end")
    mode = input("Choose Mode : ")
    if mode == "1":  
        # use current directory
        full_path = os.path.realpath(__file__)
        dir_path = os.path.dirname(full_path)
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
    elif mode == "4":
        print("Thank You!")
        countdown(3)
        return False
    else:
        print("wrong input!\n")
        directory()

# Second
def get_files(dir_path):
    # get file list in a directory
    try:
        files_names = os.listdir(dir_path)
        return files_names
    except:
        print("There are no such directory!")
        print("Your input : ", dir_path)
        return False
        

# Third
# Clean the file list to match extensions
def clean_list(files_list):
    cleaned_list = []
    for x in range(0, len(files_list)): # need to check if a file list is empty or not
        for y in range(0, len(files_extensions)):
            if files_list[x].endswith(files_extensions[y]):
                cleaned_list.append(files_list[x])
    return cleaned_list

# Fourth
# checking which to slice
def find_slice(files_names):
    if not files_names:
        print("There are no files that are available to rename")
        print("Check the extensions to make sure you've add the right extensions")
        return False
    else:
        for x in range(0, len(files_names[1])):
            print(files_names[1][x], " | ", x)
        return True

#checking for every files and every file extensions
def change_name(files_names, start, end):
    for filename in files_names:
        old_file_path = os.path.join(dir_path, filename)
        filename_new = filename[int(start):int(end) + 1]
        new_file_path = os.path.join(dir_path, filename_new)
        os.rename(old_file_path, new_file_path)
    print("Files has been renamed!")

def countdown(t): 
    while t: 
        mins, secs = divmod(t, 60) 
        #timer = '{:02d}:{:02d}'.format(mins, secs) 
        #print(timer, end="\r") 
        time.sleep(1) 
        t -= 1

while True:
    dir = directory()

    if dir == False:
        break
    else:
        files = get_files(dir)
        if files != False:
            cleaned = clean_list(get_files(dir))
            where_slice = find_slice(cleaned)
        else:
            where_slice = False
        if where_slice == False:
            if dir == False:
                break
        elif where_slice == True:
            print("Choose to slice from where to where : ")
            start = input("input start slice : ")
            print("Input big number like 999 to slice to end")
            end = input("input end slice : ")
            change_name(cleaned, start, end)
            #os.startfile(dir)