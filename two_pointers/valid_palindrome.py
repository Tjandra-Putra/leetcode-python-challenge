# 125. Valid Palindrome
"""
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""


# my own two pointer approach
def valid_palindrome(s):
    formatted_string = ""

    for char in s:
        if char.isalnum():
            formatted_string += char.lower()

    left = 0  # index
    right = len(formatted_string) - 1  # index

    while left < right:
        if formatted_string[left] != formatted_string[right]:
            return False

        left += 1
        right -= 1

    if formatted_string == " ":
        return True

    return True


print(valid_palindrome("A man, a plan, a canal: Panama"))
