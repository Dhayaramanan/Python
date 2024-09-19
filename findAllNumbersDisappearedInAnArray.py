def findDisappearedNumbers(nums):
    present = set(nums)
    result = []
    for i in range(1, len(nums) + 1):
        if i not in present:
            result.append(i)

    return result


print(findDisappearedNumbers([1, 2, 3, 2]))
