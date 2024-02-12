# Create a list of capital letters in the english alphabet
# Create a list of capital letter from the english aplhabet, but exclude 4 with the Unicode code point of either 70, 75, 80, 85.
# Create a list of capital letter from from the english aplhabet, but exclude every second between F & O

capital_letters = [chr(code) for code in range(ord('A'), ord('Z') +  1) if code not in {70,  75,  80,  85}]

print(capital_letters)

capital_letters_excluding_second = [chr(code) for code in range(ord('A'), ord('Z') +  1) if (code >= ord('F') and code <= ord('O')) == (code %  2 ==  0)]

print(capital_letters_excluding_second)