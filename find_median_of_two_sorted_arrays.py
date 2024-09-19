def findMedianOfTwoSortedArrays(nums1, nums2):
    nums = nums1 + nums2
    nums.sort()
    n = len(nums)

    mid = n // 2
    if n % 2 == 0:
        return (nums[mid] + nums[mid - 1]) / 2
    return nums[mid]


print(findMedianOfTwoSortedArrays([1, 3], [2]))
