def is_strictly_palindromic(n):
    for i in range(2, n - 1):
        val = calculate_base(n, i)
        if val[::-1] != val:
            return False
    return True


def calculate_base(n, base):
    b_n = ""
    while n > 0:
        b_n += str(n % base)
        n //= base

    return b_n[::-1]


print(is_strictly_palindromic(9))
