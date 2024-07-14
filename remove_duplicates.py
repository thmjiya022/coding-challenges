def remove_duplicates(nums):
    """
    Removes duplicate elements from a sorted array in-place.

    Args:
        nums (list): A sorted list of integers.

    Returns:
        list: A list of integers with duplicates removed.

    Example:
        >>> remove_duplicates([1,1,2,2,3,3])
        [1,2,3]
    """
    if not nums:
        return []

    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return nums[:i+1]