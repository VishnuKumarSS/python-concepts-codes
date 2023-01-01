# file handling

# ABSOLUTE PATH vs RELATIVE PATH
# The absolute path is the full path to some place on your computer. The relative path is the path
# to some file with respect to your current working directory (Print Working Directory - PWD). 
# For example:
# Absolute path:      C:/users/admin/docs/staff.txt
# If PWD is      C:/users/admin/, 
# then the relative path to staff.txt would be:   docs/staff.txt
# Note, PWD + relative path = absolute path.

import os
print(os.getcwd())
my_absolute_dirpath = os.path.abspath(os.path.dirname(__file__))
print(my_absolute_dirpath)