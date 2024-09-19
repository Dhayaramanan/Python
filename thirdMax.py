def third_max(nums):
    nums = set(nums)

    if len(nums) < 3:
        return max(nums)

    nums.remove(max(nums))
    nums.remove(max(nums))

    return max(nums)


print(third_max([2, 2, 1, 2, 3, 4]))
