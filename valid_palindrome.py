def isPalindrome(s):
    string = ""
    for i in s.lower():
        if i.isalnum():
            string += i

    rev = string[::-1]

    print(string, rev)

    for i, j in zip(string, rev):
        if i != j:
            return False

    return True


print(isPalindrome("bob"))
