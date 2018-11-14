# Have the function AlphabetSoup(str) take the str string parameter being passed.
# Return the string with the letters in alphabetical order (ie. hello becomes ehllo). 
# Assume numbers and punctuation symbols will not be included in the string. 

def AlphabetSoup(str): 
    
    # Put the characters from the string into a list
    char_list = list(str)
    
    # Sort this list into alphabetical order
    alphabetical_list = sorted(char_list)
    
    # Join all of these alphabetically ordered characters into a string 
    joined_chars = "".join(alphabetical_list)
    
    return joined_chars
    
# keep this function call here  
print AlphabetSoup(raw_input())
