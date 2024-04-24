# 1. Two Sum

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

def two_sum(nums, target):
    hash_map = {}  # complement : index

    for i, num in enumerate(nums):
        complement = target - num

        if complement in hash_map:
            return [hash_map[complement], i]

        # normal: continue to add all values in the hashmap
        hash_map[num] = i

print(two_sum([3, 2, 4], 6))
