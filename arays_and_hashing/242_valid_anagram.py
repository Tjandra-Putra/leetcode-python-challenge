# 242. Valid Anagram

"""
Input: s = "anagram", t = "nagaram"
Output: true
"""

# using sort
def is_anagram1(s, t):
    if len(s) != len(t):
        return False

    sorted_s = sorted(s)
    sorted_t = sorted(t)

    return "".join(sorted_t) == "".join(sorted_s)

# using hashmap
def is_anagram2(s,t):
    if len(s) != len(t):
        return False



print(is_anagram2("anagram", "nagaram"))
