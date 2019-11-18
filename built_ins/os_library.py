# Reference: https://towardsdatascience.com/the-treasures-of-pythons-built-in-libraries-a183f2bc6cf
# Run using: python3 built_ins/os_library.py
import os

# Execute a shell command
os.system("echo 'My name is Dipal'")

# Return the current working directory
print("Current working directory: {}".format(os.getcwd()))

# List all of the files and sub-directories in a particular folder
print("os.listdir(/): {}".format(os.listdir("/")))

# Create a single folder
os.mkdir("Trial")

# Create folders recursively
# The below line creates a folder "ttt" with a subfolder
os.makedirs("{}/built_ins/ttt".format(os.getcwd()))

# Delete a file
# os.remove("data.txt")

# Rename a file or folder
os.rename("Trial", "xyz")

# Delete a folder
os.rmdir("xyz")

# Delete directories recursively.
os.removedirs("{}/built_ins/ttt".format(os.getcwd()))


# Handling slashes / when creating file paths
file = "BuiltInFunctions.py"
folder = os.getcwd()
full_path = os.path.join(folder, file)
print("full path: {}".format(full_path))

# Get the directory and file name from a full path
print("file: {}".format(os.path.basename(full_path)))
print("folder: {}".format(os.path.dirname(full_path)))

# Check if a file or folder exists
os.path.exists(full_path)

# Get the extension of a file
name, extension = os.path.splitext(file)
