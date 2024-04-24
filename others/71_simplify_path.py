# 71. Simplify Path
"""
str = "/../abc//./def/"
"""


def simplify_path(path):
    stack = []
    path_items = path.split("/")

    for item in path_items:
        if item == "." or not item:  # empty
            continue

        elif item == "..":
            # go to previous dir
            if stack:
                stack.pop()

        else:
            # dir name
            stack.append(item)

    return "/" + "/".join(stack)


word = "/home//foo/"
word_items = word.split("/")
print(word_items)
