# 151. Reverse Words in a String
"""
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
"""


def reverse_Words(s):
    s_items = s = s.strip().split(" ")
    res = []

    for i in range(len(s_items) - 1, -1, -1):
        if s_items[i]:
            res.append(s_items[i])

    return " ".join(res)

print(reverse_Words("a good   example")
      )
