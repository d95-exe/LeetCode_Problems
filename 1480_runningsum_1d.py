class Solution:
    def runningSum(self, nums):  # Remove "list[int]"
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
sol = Solution()
nums = [1, 2, 3, 4]
print(sol.runningSum(nums))
