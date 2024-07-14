def reverse_string(s: str) -> str:
    """
    Reverse a string in place without making a copy of the array.

    Args:
    s (str): The input string to be reversed.

    Returns:
    str: The reversed string.
    """
    str_list = list(s)
    left, right = 0, len(s) - 1

    while left < right:
        str_list[left], str_list[right] = str_list[right], str_list[left]
        left += 1
        right -= 1

    return ''.join(str_list)


