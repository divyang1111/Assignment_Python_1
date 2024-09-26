# Write a Python program to test whether a passed letter is a vowel or not.

def check_vowel(letter):
    vowels = "aeiouAEIOU"  
    if letter in vowels:
        print(f"{letter} is a vowel.")
    else:
        print(f"{letter} is not a vowel.")


letter = input("Enter a letter: ")


if len(letter) == 1 and letter.isalpha():
   
    check_vowel(letter)
else:
    print("Please enter a valid single letter.")
 