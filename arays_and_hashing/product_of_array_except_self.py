# 238. Product of Array Except Self

"""
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
"""
def product_except_self2(nums):
    n = len(nums)
    bucket = [1] * n  # Initialize the bucket with 1s

    # Calculate the products to the left of each element
    left_product = 1
    for i in range(n):
        bucket[i] = left_product  # Store the product to the left in the bucket
        left_product *= nums[i]

    # bucket value will be [1,2,6, 24]

    # Calculate the products to the right of each element and update the result
    right_product = 1
    for i in range(n - 1, -1, -1): # top, lowest not inclusive of zero, stepper
        bucket[i] *= right_product  # Multiply the product to the right
        right_product *= nums[i]

    return bucket


# bucket algorithm but not allowed because of the use of division sign but it works
def product_except_self1(nums):
    product = 1
    bucket = len(nums) * [0] # [0, 0, 0, 0]

    for num in nums:
        product *= num

    for i in range(len(nums)):
        if bucket[i] == 0:
            bucket[i] = int(product / nums[i])


    return bucket

# 1,2,6,24
# 4,12,8,4
print(product_except_self2([1, 2, 3, 4]))
