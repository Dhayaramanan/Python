def rearrange_array(nums):
    new_arr = [0] * len(nums)
    pos = 0
    neg = 1
    for i in nums:
        if i > 0:
            new_arr[pos] = i
            pos += 2
        else:
            new_arr[neg] = i
            neg += 2
    return new_arr


print(rearrange_array([3, -2, -1, 1]))
