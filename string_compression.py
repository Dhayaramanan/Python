def compress(chars):
    # result = ""
    # start = 0
    # end = 0
    #
    # count = 0
    # while end < len(chars):
    #     if end == len(chars)-1:
    #         result += chars[start] + str(count+1)
    #     if chars[start] == chars[end]:
    #         count += 1
    #     else:
    #         result += chars[start] + str(count)
    #         count = 0
    #         start = end
    #         end -= 1
    #     end += 1
    #
    # print(result)
    if len(chars) == 0:
        return 0
    read = 0
    write = 0
    while read < len(chars):
        char = chars[read]
        count = 0
        while read < len(chars) and chars[read] == char:
            read += 1
            count += 1
        chars[write] = char
        write += 1

        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1
    return write


compress(["a", "a", "b", "b", "c", "c", "c"])
compress(["a","b","b","b","b","b","b","b","b","b","b","b","b","a","a"])
