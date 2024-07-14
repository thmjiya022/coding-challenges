def find_missing_number(arr):
    """
    Find the missing number in the array of distinct numbers from 0 to n.

    Args:
    arr (list): The input array of integers containing n distinct numbers taken from the range 0 to n.

    Returns:
    int: The missing number.

    Example:
    >>> find_missing_number([0, 1, 2, 4, 5])
    3
    """
    n = len(arr)
    expected_sum = (n*(n+1))//2
    actual_sum = sum(arr)

    return expected_sum - actual_sum