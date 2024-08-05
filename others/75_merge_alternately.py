def mergeAlternately(word1, word2):
    result = []
    i = 0

    while i < len(word1) or i < len(word2):
        if i < len(word1):
            result.append(word1[i])
        if i < len(word2):
            result.append(word2[i])

        i += 1

    return "".join(result)

word1 = "abc"
word2 = "pqr"

print(mergeAlternately(word1, word2))
