# Before Starting file operation following methods must be learn by a programmer
# to perform file system related methods available in os module(standard module)
# which can be used during file operations.


# 1. The rename() method used to rename the file.
# Syntax os.rename(current_file_name, new_file_name)

# 2. The remove() method to delete file.
# Syntax os.remove(file_name)

# 3.The mkdir() method of the os module to create
# directories in the current directory.
# Syntax os.mkdir("newdir")

# 4.The chdir() method to change the current directory.
# Syntax os.chdir("newdir")

# 5.The getcwd() method displays the current directory.
# Syntax os.getcwd()

# 6. The rmdir() method deletes the directory.
# Syntax os.rmdir('dirname')

import os
print(os.getcwd()) # displays current directory
os.mkdir("newdir")
os.chdir("newdir")
print(os.getcwd())