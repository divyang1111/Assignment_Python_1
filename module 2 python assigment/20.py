#  Write a Python function to insert a string in the middle of a string. 

def insert_string_middle(original_string, insert_string):
    
    middle_index = len(original_string) // 2
    
    new_string = original_string[:middle_index] + insert_string + original_string[middle_index:]
    return new_string


original = input("Enter the original string: ")
to_insert = input("Enter the string to insert: ")


result = insert_string_middle(original, to_insert)
print("New string:", result)