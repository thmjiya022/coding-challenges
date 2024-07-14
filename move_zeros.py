def move_zeros(nums):
    """
    - You must do this in-place without making a copy of the array
    - minimuze the total number of operations

    Example:
    input: [0,1,0,3,12]
    output: [1,3,12,0,0]
    """

    prev_index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            hold = nums[i]
            nums[i] = nums[prev_index]
            nums[prev_index] = hold
            prev_index+=1
    
    print(nums)