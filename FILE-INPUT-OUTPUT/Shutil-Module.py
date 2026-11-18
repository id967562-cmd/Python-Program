import shutil
#shutil.copy("my_file.txt","my_file_copy.txt")

# Define full absolute paths
# source = r"A:\SAGAR CODING STUFF\PROGRAMMING LANGUAGE\PYTHON PROGRAMMING\FILES I\FILE INPUT-OUTPUT\notes.txt"
# destination = r"A:\SAGAR CODING STUFF\PROGRAMMING LANGUAGE\PYTHON PROGRAMMING\FILES I\FILE INPUT-OUTPUT\notes_backup.txt"

# shutil.copy(source, destination)

#Suppose notes.txt is inside your current directory and you want to move it into the python
shutil.move("notes.txt","Python/notes.txt")