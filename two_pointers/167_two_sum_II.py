# 167. Two Sum II - Input Array Is Sorted
"""
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
"""


# rmb to plus one to index for result before returning

def two_sum(numbers, target):
    left = 0
    right = len(numbers) - 1  # index

    # array must be sorted to work
    while left < right:
        total = numbers[left] + numbers[right]

        if total == target:
            return [left + 1, right + 1]

        elif total > target:
            right -= 1

        else:
            left += 1


print(two_sum([2, 7, 11, 15], 9))
