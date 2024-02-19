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
os.makedirs(folder_name, exist_ok=True)

# Step 2: In that folder, create a file named 'exercise.py'
file_name = 'exercise.py'
file_path = os.path.join(folder_name, file_name)

# Step 3: Get input from the console and write it to the file
user_input = input("Enter some text to write to the file: ")
with open(file_path, 'w') as file:
    file.write(user_input)

# Step 4: Repeat step 2 and 3 (name the file something else)
new_file_name = 'exercise2.py'
new_file_path = os.path.join(folder_name, new_file_name)

with open(new_file_path, 'w') as new_file:
    pass  # Creating an empty file for demonstration purposes

new_user_input = input("Enter some text for the second file: ")
with open(new_file_path, 'w') as new_file:
    new_file.write(new_user_input)

# Step 5: Read the content of the files and print it to the console
for file_name in [file_name, new_file_name]:
    file_path = os.path.join(folder_name, file_name)
    with open(file_path, 'r') as file:
        file_content = file.read()
        print(f"Content of '{file_name}': {file_content}")
