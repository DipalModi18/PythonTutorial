import os

filename = input("Enter filename: ")
print('File name: ', filename)

try:
    file = open(filename, 'a+')  # Opens a file for both appending and reading
    print("Name of the file: ", file.name)
    print("Closed or not : ", file.closed)
    print("Opening mode : ", file.mode)
except IOError as argument:
    # An exception can have an argument, which is a value that gives additional information about the problem.
    print('Error while opening the file: ', filename)
    print('Additional info: ', argument)
    file.close()
else:
    """The code in the else-block executes if the code in the try: block does not raise an exception."""
    print("Opened file successfully")
# You can provide except clause(s), or a finally clause, but not both.
# You cannot use else clause as well along with a finally clause.


file.write(input("Enter string to write in the file: "))

print("Current position: ", file.tell())

file.seek(0, 0)
# By default, a+ opens file and file pointer is at the end of the file to append.
# By seek method (bytes_to_move, reference_point) moves pointer from the reference_point to bytes_to_move bytes far.
# reference_point is an optional argument
str1 = file.read()
print('\n Read str is: ', str1)

# Python os module provides methods that help you perform file-processing operations,
#           such as renaming and deleting files.
# os.rename(current_file_name, new_file_name)
os.rename(filename, "my1.txt")


# You can use the remove() method to delete files by supplying the name of the file to be deleted as the argument.
# os.remove(file.name)


# The os module has several methods that help you create, remove, and change directories.
# mkdir() method of the os module to create directories in the current directory.
os.mkdir("MyDirectory")

# rmdir() method deletes the directory
os.rmdir("MyDirectory")

# chdir() method to change the current directory.
# os.chdir("newdir")


print("Current working directory: ", os.getcwd())
file.close()
