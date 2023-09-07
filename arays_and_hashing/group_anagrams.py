# 49. Group Anagrams
"""
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

def group_anagrams(strs):
    hashmap = {}
    result = []

    for word in strs:
        sorted_word = "".join(sorted(word))

        if not sorted_word in hashmap:
            hashmap[sorted_word] = [word]
        else:
            hashmap[sorted_word].append(word)

    for key, value in hashmap.items():
        result.append(value)

    return result


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
