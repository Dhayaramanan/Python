def compress(chars):
    char_set = {}
    result = ""
    for i in chars:
        if i in char_set:
            char_set[i] += 1
        else:
            char_set[i] = 1

    for char, count in zip(char_set.keys(), char_set.values()):
        if count == 1:
            result += char
        else:
            result += char + str(count)

    print(result)
    chars[:len(result)] = list(result)
    print(chars)
    return len(result)


print(compress(["a", "a", "b", "b", "c", "c", "c"]))
