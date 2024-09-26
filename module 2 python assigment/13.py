'''Write a Python program to count the occurrences of each word in a 
given sentence '''

def count_word_occurrences(sentence):
    
    words = sentence.split()
    
   
    word_count = {}
    
    for word in words:
        
        word = word.lower()
        
        
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            
    return word_count


user_sentence = input("Enter a sentence: ")


occurrences = count_word_occurrences(user_sentence)
print("Word occurrences:")
for word, count in occurrences.items():
    print(f"'{word}': {count}")