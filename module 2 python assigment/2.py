 # Write a Python program to get the Factorial number of given number. 
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

number = int(input("Enter a number: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    
     print(f"The factorial of {number} is {factorial(number)}.") 