def pivotArray(nums, pivot):
    less_than_pivot = []
    equal_to_pivot = []
    greater_than_pivot = []

    for i in nums:
        if i < pivot:
            less_than_pivot.append(i)
        elif i > pivot:
            greater_than_pivot.append(i)
        else:
            equal_to_pivot.append(i)
    return less_than_pivot + equal_to_pivot + greater_than_pivot


print(pivotArray([9, 12, 5, 10, 3, 14, 10], 10))
