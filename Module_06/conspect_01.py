from os import makedirs
from shutil import copyfile, move
# Create a new folder for the way
makedirs(r'C:\Users\nsher\Documents\! VSCode Projects\Learn_Python\Module_06\Test_dir', exist_ok=True)
# Creating new file.
file = open(
    r'C:\Users\nsher\Documents\! VSCode Projects\New project\text111.txt', 'w')
file.close()

# Copying a file to a new folder for the way
copyfile(r'C:\Users\nsher\Documents\! VSCode Projects\New project\text111.txt',
         r'C:\Users\nsher\Documents\! VSCode Projects\Learn_Python\Module_06\Test_dir\text111.txt')

# Moved file from Module_06 to Module_04 - and also rename file
move(r'C:\Users\nsher\Documents\! VSCode Projects\Learn_Python\Module_06\Test_dir\text111.txt',
     r'C:\Users\nsher\Documents\! VSCode Projects\Module_04\moved_file_test.txt')
