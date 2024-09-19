def reverseVowels(s):
    vowels = 'aeiouAEIOU'
    s_list = list(s)

    start = 0
    end = len(s) - 1

    while start <= end:
        if s_list[start] in vowels and s_list[end] in vowels:
            s_list[start], s_list[end] = s_list[end], s_list[start]
            end -= 1
            start += 1

        elif s_list[start] in vowels:
            end -= 1
        else:
            start += 1

    return ''.join(s_list)


print(reverseVowels('race car'))
