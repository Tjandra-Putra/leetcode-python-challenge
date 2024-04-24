# 347. Top K Frequent Elements

"""
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
"""


def top_k_frequent(nums, k):
    frequency = {}  # num : frequency
    output = []

    for num in nums:
        if not num in frequency:
            frequency[num] = 1

        else:
            frequency[num] += 1

    sorted_dict_frequency = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))

    count = 0
    for key in sorted_dict_frequency:
        if count < k:
            output.append(key)
            count += 1

    return output


print(top_k_frequent([5, 1, 1, 1, 2, 2, 3, 3, 3, 3], 2))
