# Ex: Sort a Text
# Solution
#
# Create a function that takes a string as a parameter and returns a list.
#
# The function should remove all vowels and sort the consonants in alphabetic order, and the return the result.

def sort_consonants(text):
    # Step  2: Use a list comprehension to exclude vowels
    consonants = [char for char in text if char.lower() not in 'aeiou']
    
    # Step  3: Eliminate duplicates and sort the consonants
    consonants = sorted(set(consonants))
    
    # Step  5: Return the sorted list of consonants
    return consonants

# Example usage:
text = "example"
result = sort_consonants(text)
print(result)  # Output: ['e', 'm', 'p', 'x']
