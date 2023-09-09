# 11. Container With Most Water
"""

"""


def max_area(height):
    l, r = 0, len(height) - 1
    max_area = 0

    while l < r:
        width = r - l
        current_area = min(height[l], height[r]) * width
        max_area = max(current_area, max_area)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return max_area


# == got mistake cannot pass all test cases ==
# def max_area(height):
#     l, r = 0, len(height) - 1
#     max_area = 0
#
#     for i in range(len(height)):
#         if l < r:
#             width = r - l
#             current_area = min(height[l], height[r]) * width
#
#             if current_area > max_area:
#                 max_area = current_area
#
#             if l > r:
#                 r -= 1
#             else:
#                 l += 1
#
#     return max_area


print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
