def frequent_word(words):
    if not words:
        return None
    
    higest_count = 0
    most_frequent_word = None
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
        
        if word_count[word] > higest_count:
            most_frequent_word = word
    
    return most_frequent_word