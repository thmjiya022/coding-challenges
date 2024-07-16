def average_length_strings(words):
    if not words:
        return 0
    
    return sum(len(word) for word in words) / len(words)
