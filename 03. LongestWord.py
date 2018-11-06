# Have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string. 
# If there are two or more words that are the same length, return the first word from the string with that length. 
# Ignore punctuation and assume sen will not be empty. 

import string

def LongestWord(sen):
    ascii = string.ascii_letters
    newStr = ""

    # Remove all non-ascii characters from the string
    for letter in sen:
        if letter in ascii or letter == " ":
            newStr += letter
        
    # Split the sentence into individual words and add them to a list
    separateWords = newStr.split(" ")

    # Use built in Python function, max, using length as a parameter of key to find the longest word
    longest = max(separateWords, key=len)
    return longest
        
        
# keep this function call here  
print(LongestWord(raw_input()))
