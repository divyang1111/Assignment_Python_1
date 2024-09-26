'''Write a Python function that takes a list of words and returns the length 
of the longest one. '''

def longest_word_length(words):
    if not words: 
        return 0
    return max(len(word) for word in words)  

word_list = ["apple", "banana", "cherry", "date"]
result = longest_word_length(word_list)
print("The length of the longest word is:", result)