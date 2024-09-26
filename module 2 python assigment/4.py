'''Write python program that swap two number with temp variable and 
without temp variable.'''

def swap_without_temp(a, b):
    print(f"Before swapping: a = {a}, b = {b}")
    a, b = b, a  
    print(f"After swapping: a = {a}, b = {b}")


a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))


swap_without_temp(a, b)
