from math import gcd


def gcdOfStrings(str1: str, str2: str) -> str:
    if (str1 + str2) != (str2 + str1):
        return ""
    return str1[:gcd(len(str1), len(str2))]


print(gcdOfStrings("ABABAB", "ABABABAB"))
