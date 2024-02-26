import os

# Get the directory of the script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Define the filename
# os.path.join (<directory>, <file name>)
filename = os.path.join(script_directory, "numbers.dat")

# step 1 write to file
with open(filename, 'w') as file:
    #laver en range af tal vi skal bruge (for range loop)
    # vi behøver ikke at angive datatypen den skal skrive, kun variablen. Datatypen regner den selv ud, når vi skriver in range (<int>,<int>)
    for number in range (1,101):
        #skriver range af tal til fil   
        #husk at caste int til en string
     file.write(str(number) + "\n")
      
    

#step 2 read from file
with open(filename, 'r') as file:
# laver en liste med int som indeholder alle tallene fra filen. 
# Vi skal huske at strip, for at undgå at få whitespaces med. Husk at angive datatypen inde i listen
# hint. du kan lave et for loop inde i listen. Husk at bruge line, da python returnere et itterable object
    numbers = [int(line.strip()) for line in file]
    
    # vi laver en liste som indeholder alle lige tal,
    # vi bruger modulus for at se om talle er lige og skal tilføjes
    # vi laver en ny liste hvor vi sammentidig gennemløber den første
    # husk du kan lave et for loop inde i en liste
    even_numbers = [num for num in numbers if num % 2 == 0]
    print("even numbers: ",even_numbers)
 
 
    
 
    