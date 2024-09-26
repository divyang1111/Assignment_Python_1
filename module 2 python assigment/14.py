'''Write a Python program to get a single string from two given strings, 
separated by a space and swap the first two characters of each string.  '''

def swap_and_combine(string1, string2):
    
    if len(string1) < 2 or len(string2) < 2:
        return "Both strings must have at least two characters."
    
    swapped_string1 = string2[:2] + string1[2:] 
    swapped_string2 = string1[:2] + string2[2:]  
    
    combined_string = swapped_string1 + " " + swapped_string2
    return combined_string


str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")


result = swap_and_combine(str1, str2)
print("Resulting string:", result)