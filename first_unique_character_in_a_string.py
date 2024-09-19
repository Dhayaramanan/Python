from collections import Counter


def firstUniqChar(s):
    count = Counter(s)
    for i in count:
        if count[i] == 1:
            return s.index(i)

    return -1


print(firstUniqChar("leetcode"))
