def is_palindrome(x: int) -> bool:
    """
    Checks if a given integer is a palindrome.

    A palindrome is a number or a text phrase that reads the same backwards as forwards.
    For example, the number 12321 is a palindrome.

    Args:
        x (int): The input integer to check.

    Returns:
        bool: True if the input integer is a palindrome, False otherwise.

    Example:
        >>> is_palindrome(121)
        True
    """
    if x < 0:
        return False
    
    string_x = str(x).lower()
    reversed_word = ''

    for i in range(len(string_x)-1, -1, -1):
        reversed_word += string_x[i]

    return string_x == reversed_word

print(is_palindrome(121))