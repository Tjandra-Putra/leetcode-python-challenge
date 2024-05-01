# 217. Contains Duplicate

# Input: nums = [1,2,3,1]
# Output: true

# using set
def contains_duplicate1(nums):
    num_set = set()

    for num in nums:
        if num in num_set:
            return True

        num_set.add(num)

    return False

# using hashmap
def contains_duplicate2(nums):
    hashmap = {}

    for num in nums:
        if num in hashmap:
            return True

        else:
            hashmap[num] = 0

    return False

print(contains_duplicate2([5, 2, 4, 1,2]))

# using set and comparing the length
def contains_duplicate3(nums):
    unique_nums = set(nums)

    if len(unique_nums) == len(nums):
        return False
        
    return True