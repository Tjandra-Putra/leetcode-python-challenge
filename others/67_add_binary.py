# 67. Add Binary

def add_binary(a, b):
    res = ""
    carry = 0

    a, b = a[::-1], b[::-1]  # reverse

    for i in range(max(len(a), len(b))):  # iterate through longest
        digitA = int(a[i]) if i < len(a) else 0
        digitB = int(b[i]) if i < len(b) else 0

        total = digitA + digitB + carry
        char = str(total % 2)
        res = char + res
        carry = total // 2

    if carry:
        res = "1" + res

    return res


print(add_binary("1010", "1011"))
