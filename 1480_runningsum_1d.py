class Solution:
    def runningSum(self, nums):  # Remove "list[int]"
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
