#  Write a Python function to reverses a string if its length is a multiple of 4. 
 
def reverse_string_if_multiple_of_four(input_string):
    if len(input_string) % 4 == 0:
        return input_string[::-1]  
    else:
        return input_string 

user_string = input("Enter a string: ")
result = reverse_string_if_multiple_of_four(user_string)
print("Resulting string:", result)