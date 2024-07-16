def string_with_most_vowels(words):
    def count_vowels(word):
        return sum(1 for letter in word if letter in 'aeiou')
    
    most_vowels_count = 0
    word_with_most_vowels = None

    for word in words:
        if count_vowels(word) > most_vowels_count:
            most_vowels_count = count_vowels(word)
            word_with_most_vowels = word
    
    return word_with_most_vowels