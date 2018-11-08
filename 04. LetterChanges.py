# Have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm. 
# Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a). 
# Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string. 

from string import ascii_letters
from string import ascii_uppercase

def LetterChanges(str): 
  
    # Initialise a new string to create a new sentence after the letters have been replaced   
    new_string = ""
    
    # Find the location of each letter from the original string in the ascii string
    for letter in str:
        # Check to see if the letter is in the alphabet 
        if letter in (ascii_letters or ascii_uppercase):
            # Find its position in the ascii_letters string 
            ascii_position = ascii_letters.find(letter)
            # Move the position up by one and add the ascii letter at this location to the new string 
            new_string += ascii_letters[ascii_position + 1]
        # If the letter is not in the alphabet (e.g. a special character or a number), add it to the new string as normal
        else:
            new_string += letter
    
    for letter in new_string:
        # Check to see if the letter is a vowel
        if letter in ('a', 'e', 'i', 'o', 'u'):
            # If it is a lowercase vowel, replace it with a capitalized version
            new_string = new_string.replace(letter, letter.upper())
    return new_string


# keep this function call here  
print(LetterChanges(raw_input()))
