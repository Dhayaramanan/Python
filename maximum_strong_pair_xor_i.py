class Solution:
    def maximum_strong_pair_xor(self, nums):
        max_xor = 0
        for i in range(len(nums) - 1):
            for j in range(i, len(nums)):
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                    max_xor = max(max_xor, (nums[i] ^ nums[j]))

        return max_xor


sol = Solution()
print(sol.maximum_strong_pair_xor([1, 2, 3, 4, 5]))
print(sol.maximum_strong_pair_xor([1, 1, 10, 3, 9]))
