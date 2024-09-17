#using ai Write a python program to print the contents of a directory using the os module. 
#Search online for the function which does that.
import os

def print_directory_contents(path):
    try:
        # List the contents of the directory
        contents = os.listdir(path)
        
        # Print each item in the directory
        for item in contents:
            print(item)
    except FileNotFoundError:
        print("The directory does not exist.")
    except PermissionError:
        print("You do not have permission to access this directory.")

# Specify the path to the directory
directory_path = 'd:'  # Current directory

# Call the function to print the directory contents
print_directory_contents(directory_path)
