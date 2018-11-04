# Using the Python language, have the function FirstFactorial(num) take the num parameter being passed and return the factorial of it.

def FirstFactorial(num): 

    # base case
    if num == 1:
        return num
    else:
        factorial = num * FirstFactorial(num-1)
        return factorial
   
print(FirstFactorial(raw_input()))
