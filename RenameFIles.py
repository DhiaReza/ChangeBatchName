# TO DO
# Add an extra file to store extensions
# add confirmation before renaming
# add history system
# add custom names instead of just slicing ( use var.replace() and then var.strip() )
# add fail safe to guard from files that has different character length ex : myfile1, my file03, my file11

#How to build :
# pyinstaller -F RenameFiles.py

import os
import time

# file extensions to check
files_extensions = [".mp4", ".mkv"]

# file directory
dir_path = ""

# first
#choose directory
def choose_directory():
    global dir_path
    print("List of modes:")
    print("1 to use current directory")
    print("2 to use user input directory")
    print("3 to add file extensions to check")
    print("4 to end")
    mode = input("Choose Mode: ")
    if mode == "1":
        full_path = os.path.realpath(__file__)
        dir_path = os.path.dirname(full_path)
    elif mode == "2":
        dir_path = input("Copy and Paste your directory here: ")
    elif mode == "3":
        add_extensions()
        choose_directory()
    elif mode == "4":
        print("Thank You!")
        countdown(3)
        return False
    else:
        print("Wrong input!\n")
        choose_directory()
    return dir_path

#use current directory
def current_dir():
    # use current directory
    full_path = os.path.realpath(__file__)
    dir_path = os.path.dirname(full_path)
    global dir
    dir = dir_path
    return dir_path

#use custom directory
def custom_dir():
    # user inputed directory
    dir_path = input("Copy and Paste you directory here : ")
    global dir
    dir = dir_path
    return dir_path

# Add file extensions to check
def add_extensions():
    print("Current extensions to check: ", files_extensions)
    more_ext = input("Input extensions here (example: .mp3): ")
    files_extensions.append(more_ext)
    print(f"{more_ext} has been added")

# Second
def get_files(dir_path):
    # get file list in a directory
    try:
        files_names = os.listdir(dir_path)
        print("Your Files : ")
        for x in files_names:
            print((files_names.index(x)+1),". ",x)
        print("")
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
        print("")
        return False
    else:
        for x in range(0, len(files_names[1])):
            print(files_names[1][x], " | ", x)
        return True

# fifth
# renaming files by slicing
def rename_files_slice(files_names, start, end):
    for filename in files_names:
        old_file_path = os.path.join(dir_path, filename)
        filename_new = filename[int(start):int(end) + 1]
        new_file_path = os.path.join(dir_path, filename_new)
        os.rename(old_file_path, new_file_path)
    print("Files has been renamed!")

# sixth
# or Rename files using replace
def rename_files_replace(files_names, old_str, new_str):
    for filename in files_names:
        old_file_path = os.path.join(dir_path, filename)
        filename_new = filename.replace(old_str, new_str)
        new_file_path = os.path.join(dir_path, filename_new)
        os.rename(old_file_path, new_file_path)
    print("Files have been renamed using replace!")

def countdown(t): 
    while t: 
        #mins, secs = divmod(t, 60) 
        #timer = '{:02d}:{:02d}'.format(mins, secs) 
        #print(timer, end="\r") 
        time.sleep(1) 
        t -= 1

def check_input(start, end):
    while True:
        try:
            start_slice = int(input(start))
            end_slice = int(input(end))
            if start_slice >= 0 and end_slice >= 0:
                return start_slice, end_slice
            else:
                print("Your input number is less than 0. Please enter numbers greater than or equal to 0.\n")
        except ValueError:
            print("Your input is not a number. Please enter a valid number.\n")

# Main function
def main():
    while True:
        global dir_path
        dir_path = choose_directory()

        if not dir_path:
            break
        else:
            files = get_files(dir_path)
            if files:
                cleaned = clean_list(files)
                if not cleaned:
                    print("There are no files that match the extensions.")
                    continue

                print("Choose Operation Mode:")
                print("1 for slicing")
                print("2 for replacing")
                mode = input("Choose Mode: ")

                if mode == "1":
                    for x in range(0, len(cleaned[0])):
                        print(cleaned[0][x], " | ", x)
                    start, end = check_input("Input start slice: ", "Input end slice: ")
                    rename_files_slice(cleaned, start, end)
                elif mode == "2":
                    old_str = input("Enter the string to replace: ")
                    new_str = input("Enter the new string: (don't type anything to delete the string)")
                    rename_files_replace(cleaned, old_str, new_str)
                else:
                    print("Wrong input!\n")
            else:
                continue

if __name__ == "__main__":
    main()