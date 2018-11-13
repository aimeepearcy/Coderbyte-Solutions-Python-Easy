# Have the function TimeConvert(num) take the num parameter being passed.
# Return the number of hours and minutes the parameter converts to (ie. if num = 63 then the output should be 1:3). 
# Separate the number of hours and minutes with a colon. 

import math

# The num variable represents the length of time in minutes
def TimeConvert(num): 
    
    # To get the time in hours from the time in mins, divide by 60 and round down
    time_in_hours = int(math.floor(num / 60))
    
    # To get the number of minutes remaining
    time_in_mins_remaining = num % 60
    
    return str(time_in_hours) + ":" + str(time_in_mins_remaining)
    
# keep this function call here  
print TimeConvert(raw_input())  
