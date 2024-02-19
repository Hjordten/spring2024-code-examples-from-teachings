import os

# Get the directory of the script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Define the filename
filename = os.path.join(script_directory, "numbers.dat")

# step 1 write to file
with open (filename, "w") as file:
    #laver en range af tal vi skal bruge
    for number in range (1, 101):
        file.write(str(number) + "\n")
    

#step 2 read from file
with open (filename, "r") as file:
#laver en liste med int som indeholder alle tallene fra filen. Vi skal huske at strip, for at undgå at få whitespaces med
    numbers = [int(line.strip()) for line in file]
    
    # vi laver en liste som indeholder alle lige tal, vi bruger modulus for at se om talle er lige og skal tilføjes
    # vi laver en ny liste hvor vi sammentidig gennemløber den første
    even_numbers = [num for num in numbers if num % 2 == 0]
    print("even numbers:", even_numbers)

    