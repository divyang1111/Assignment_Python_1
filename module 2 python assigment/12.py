# Write a Python program to count occurrences of a substring in a string. 

def count_substring(string, substring):
    return string.count(substring)  


main_string = input("Enter the main string: ")
substring = input("Enter the substring to count: ")


occurrences = count_substring(main_string, substring)
print(f"The substring '{substring}' occurs {occurrences} times in the main string.")