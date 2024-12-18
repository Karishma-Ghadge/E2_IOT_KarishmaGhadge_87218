def find_longest_word(words):
   
    longest_length = 0
   
    for word in words:
        
        if len(word) > longest_length:
            longest_length = len(word)
    
    return longest_length

words_list = ["RED", "GREEN", "YELLOW", "PINK", "BLACK"]

longest_word_length = find_longest_word(words_list)

print("The length of the longest word is : ", longest_word_length)