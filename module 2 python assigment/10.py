# Write a Python program to calculate the length of a string. 

def calculate_length(string):
    return len(string) 

user_input = input("Enter a string: ")


length = calculate_length(user_input)
print(f"The length of the string is: {length}")