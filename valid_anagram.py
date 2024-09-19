from collections import Counter


def isAnagram(s, t):
    if len(s) != len(t):
        return False

    s_counter = Counter(s)
    t_counter = Counter(t)

    for i in s_counter:
        if i not in t_counter or s_counter[i] != t_counter[i]:
            return False

    return True


print(isAnagram("anagram", "naagarm"))
