def replaceWords(dictionary, sentence):
    result = ""
    split_sentence = sentence.split()
    maps = {}

    # to get root words of a word if exists
    for i in dictionary:
        for j in split_sentence:
            if j.startswith(i) and j not in maps:
                maps[j] = [i]
            elif j.startswith(i) and j in maps:
                maps[j].append(i)

    # to append all the words in order they appear in sentence
    for i in split_sentence:
        # replace the word if there's an alternative
        if i in maps:
            maps[i].sort()
            result += " " + maps[i][0]  # sorted list for getting the shortest root word
        else:
            result += " " + i

    return result.strip()


print(replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery"))
print(replaceWords(["a", "b", "c"], "aadsfasf absbs bbab cadsfafs"))
