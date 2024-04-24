# 14. Longest Common Prefix
"""
Input: strs = ["flower","flow","flight"]
Output: "fl"
"""


def longest_common_prefix(strs):
    if len(strs) == 0:
        return ""

    if len(strs) == 1:
        return strs[0]

    prefix = strs[0]  # first word in the list
    prefix_length = len(prefix)

    for s in strs[1:]:
        while prefix != s[0:prefix_length]:
            prefix = prefix[0:prefix_length - 1]
            prefix_length -= 1

            if prefix_length == 0:
                return ""  # no common prefix

    return prefix


print(longest_common_prefix(["dog","racecar","car"])
      )

