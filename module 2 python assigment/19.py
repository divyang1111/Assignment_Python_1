'''Write a Python program to get a string made of the first 2 and the last 
2 chars from a given a string. If the string length is less than 2, return 
instead of the empty string.  '''

def first_and_last_two_chars(input_string):
    if len(input_string) < 2:
        return "String length is less than 2." 
    else:
        return input_string[:2] + input_string[-2:]  


user_string = input("Enter a string: ")


result = first_and_last_two_chars(user_string)
print("Resulting string:", result)