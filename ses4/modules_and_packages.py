# Do the following task using the os module

#1. create a folder and name the folder 'os_exercises.'                                                  
#2. In that folder create a file. Name the file 'exercise.py'                                                                            
#3. get input from the console and write it to the file.                                                 
#    * In VSCode and using Notebooks the console will pop up in the top of the editor. So ```input()``` will propt the user for input, and i VScode this is in the top of the editor. 
#4. repeat step 2 and 3 (name the file something else).                                                  
#5. read the content of the files and and print it to the console.

import os

# Step 1: Create a folder named 'os_exercises'
folder_name = 'os_exercises'
# use os."find it out", remember exists_ok=True
os.makedirs(folder_name, exist_ok=True)

# Step 2: In that folder, create a file named 'exercise.py'
file_name = 'exercise.py'
# hint, you need the join the folder and file
file_path = os.path.join(folder_name, file_name)

# Step 3: Get input from the console and write it to the file
# make a input, and give the text "enter some text to write to the file: "
user_input = input("Enter some text to write to the file: ")
# write to file
with open(file_path, 'w') as file:
    #write user input to file
    file.write(user_input)

# Step 4: Repeat step 2 and 3 (name the file something else)
new_file_name = 'exercise2.py'
new_file_path = os.path.join(folder_name, new_file_name)

new_user_input = input("Enter some text for the second file: ")
with open(new_file_path, 'w') as new_file:
    new_file.write(new_user_input)

# Step 5: Read the content of the files and print it to the console
# We make a list that is the two paths to the two files we need to read
# we make a for in loop because of more advantages
for file_name in [file_name, new_file_name]:
    # We join the folder and file 
    file_path = os.path.join(folder_name, file_name)
    # we open the file to reading
    with open(file_path, 'r') as file:
        #we read the file
        file_content = file.read()
        # we print the file name and its file content with a formatted print
        print(f"Content of '{file_name}': {file_content}")
