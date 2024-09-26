'''Write a Python program to add 'ing' at the end of a given string (length 
should be at least 3). If the given string already ends with 'ing' then add 
'ly' instead if the string length of the given string is less than 3, leave it 
unchanged.  '''

def modify_string(input_string):
    if len(input_string) < 3:
        return input_string  
    elif input_string.endswith('ing'):
        return input_string + 'ly'  
    else:
        return input_string + 'ing'  


user_string = input("Enter a string: ")


result = modify_string(user_string)
print("Modified string:", result)