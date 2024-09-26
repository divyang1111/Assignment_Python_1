''' Write a Python program to find the first appearance of the substring 
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the 
whole 'not'...'poor' substring  with 'good'. Return the resulting string.'''

def replace_not_poor(input_string):
    not_index = input_string.find('not')
    poor_index = input_string.find('poor')
    
    
    if not_index != -1 and poor_index != -1 and not_index < poor_index:
        
        return input_string[:not_index] + 'good' + input_string[poor_index + len('poor'):]
    else:
        return input_string  


user_string = input("Enter a string: ")


result = replace_not_poor(user_string)
print("Resulting string:", result)  