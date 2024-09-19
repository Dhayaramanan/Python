import collections


def kthDistinct(arr, k):
    ele = collections.Counter(arr)

    # for i in arr:
    #     if i in ele:
    #         ele[i] = False
    #     else:
    #         ele[i] = True

    # l = [i for i in ele.keys() if ele[i]]
    #
    # if len(l) < k:
    #     return ""
    #
    # return l[k - 1]

    count = 0
    for i in ele.keys():
        if ele[i] == 1:
            count += 1
        if count == k:
            return i

    return ""


print(kthDistinct(["d", "b", "c", "b", "c", "a"], 2))
