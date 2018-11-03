# Have the function FirstReverse(str) take the str parameter being passed and return the string in reversed order. 
# For example: if the input string is "Hello World and Coders" then your program should return the string sredoC dna dlroW olleH. 

def FirstReverse(str): 
# Reverse string using extended slice 
    reverse_str = str[::-1]
    return reverse_str

print(FirstReverse(raw_input()))
