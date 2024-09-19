def min_pair_sum(nums):
    nums.sort()
    i = 0
    j = len(nums) - 1

    pairs = []

    while i <= j:
        pairs.append([nums[i], nums[j]])
        i += 1
        j -= 1

    return max(sum(i) for i in pairs)


print(min_pair_sum([3, 5, 2, 3]))
print(min_pair_sum([3, 5, 4, 2, 4, 6]))

"""
def min_pair_sum(nums):
        nums.sort()
        i = 0
        j = len(nums) - 1

        max_sum = 0

        while i <= j:
            t_sum = sum([nums[i], nums[j]])
            if t_sum > max_sum:
                max_sum = t_sum
            i += 1
            j -= 1

        return max_sum
"""