# Have the function SimpleSymbols(str) take the str parameter being passed.
# Determine if it is an acceptable sequence by either returning the string true or false. 
# The str parameter will be composed of + and = symbols with several letters between them (ie. ++d+===+c++==a).
# For the string to be true each letter must be surrounded by a + symbol. So the string to the left would be false. 
# The string will not be empty and will have at least one letter. 

def SimpleSymbols(str): 
 
    # If the first or last letter in the string is an alphabetic character.
    # It can't be surrounded by '+' characters, so return false.
    if str[0].isalpha() or str[len(str)-1].isalpha():
        return "false"
        
    # Iterate through the string and check if each letter is in the alphabet. 
    # If it is, check that the surrounding characters are "+"s.
    for i in range(1, len(str)):
        if str[i].isalpha():
            if str[i-1] != "+":
                return "false"
            if str[i+1] != "+":
                return "false"
                
    # If none of these are the case, the string must be acceptable by default.
    return "true"
    
# keep this function call here  
print SimpleSymbols(raw_input())
