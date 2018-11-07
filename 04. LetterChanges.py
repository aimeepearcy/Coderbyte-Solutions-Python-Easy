from string import ascii_letters
from string import ascii_uppercase

def LetterChanges(str): 
  
    # Initialise a new string to create a new sentence after the letters have been replaced   
    new_string = ""
    
    # Find the location of each letter from the original string in the ascii string
    for letter in str:
        ascii_position = ascii_letters.find(letter)
        # Add the ascii letter at this location to the new string 
        new_string += ascii_letters[ascii_position + 1]
    print(new_string)
    
    # Capitalize the vowels
    for letter in new_string:
        if letter == 'a' or 'e' or 'i' or 'o' or 'u':
            new_string = new_string.replace(letter, letter.upper())
        else:
            pass
    print(new_string)


# keep this function call here  
print(LetterChanges("cat!!"))
















  
