def product_except_self(nums):
    """
    Calculate the product of array except self using a brute-force approach.
    
    Args:
    nums (list of int): Input array of integers.
    
    Returns:
    list of int: Output array where each element is the product of all elements in nums except itself.
    """
    output = []
    
    def do_product(nums, number):
        product = 1
        for i in range(len(nums)):
            if nums[i] == number:
                continue
            product *= nums[i]
        return product
   
    for number in nums:
        output.append(do_product(nums, number))
       
    return output

def product_except_self(nums):
    """
    Calculate the product of array except self using a brute-force approach.
    
    Args:
    nums (list of int): Input array of integers.
    
    Returns:
    list of int: Output array where each element is the product of all elements in nums except itself.
    """
    output = []
    
    def do_product(nums, number):
        product = 1
        for i in range(len(nums)):
            if nums[i] == number:
                continue
            product *= nums[i]
        return product
   
    for number in nums:
        output.append(do_product(nums, number))
       
    return output

# Example usage
nums = [1, 2, 3, 4]
output = product_except_self(nums)
print(output)  # Output: [24, 12, 8, 6]
