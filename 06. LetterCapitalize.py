# Have the function LetterCapitalize(str) take the str parameter being passed and capitalize the first letter of each word. 
# Words will be separated by only one space. 

def LetterCapitalize(str): 
    
    # Create a new string placeholder to store the updated values
    new_str = ""
    
    # Split the string so each word is separate
    str = str.split()
    for word in str:
            # The .capitalize() function capitalizes the first word in each string
            new_word = word.capitalize()
            # Add the updated word to the new_str placeholder, along with a space to separate them
            new_str += " " + new_word
    # The first letter will always be a space, so remove it and then return the completed string
    return new_str[1:]
    
# keep this function call here  
print LetterCapitalize(raw_input())
