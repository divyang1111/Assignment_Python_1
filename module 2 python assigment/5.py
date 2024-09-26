''' Write a Python program to find whether a given number is even or odd, 
print out an appropriate message to the user. '''

def check_even_odd(num):
    if num % 2 == 0:
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")


number = int(input("Enter a number: "))


check_even_odd(number)