def find_longest_word(words):
    if not words:
        return None
    return max(words, key=len)
