''' Write a Python program to count the number of characters (character 
frequency) in a string  '''

def character_frequency(string):
    frequency = {}  
    for char in string:
        if char in frequency:
            frequency[char] += 1  
        else:
            frequency[char] = 1  
    return frequency


user_input = input("Enter a string: ")


frequency_count = character_frequency(user_input)
print("Character frequency in the string:")
for char, count in frequency_count.items():
    print(f"'{char}': {count}")