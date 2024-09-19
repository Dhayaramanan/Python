def titleToNumber(column_title):
    # number = 0
    # val = 1
    # for i in column_title[::-1]:
    #     number += (ord(i) - 65 + 1) * val
    #     val *= 26
    number = 0

    for ch in column_title:
        number = number * 26 + (ord(ch) - 65 + 1)

    return number


def main():
    print(titleToNumber("A"))
    print(titleToNumber("AAB"))
    print(titleToNumber("ZY"))


if __name__ == '__main__':
    main()
