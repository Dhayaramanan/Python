def convertToTitle(column_number):
    string = ""

    while column_number > 0:
        column_number -= 1
        string += chr(65 + column_number % 26)
        column_number //= 26

    return string[::-1]


def main():
    print(convertToTitle(701))
    print(convertToTitle(26))
    print(convertToTitle(1))
    print(convertToTitle(1242321312))


if __name__ == '__main__':
    main()
