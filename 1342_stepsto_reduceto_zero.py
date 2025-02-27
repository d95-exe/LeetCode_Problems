class Solution:
    def numberOfSteps(self, num) -> int:
        steps = 0
        while num != 0:
            if num%2 == 0:
                num = num/2
                steps += 1
            else:
                num = num-1
                steps += 1
        return steps

sol = Solution()
num= 3
print(sol.numberOfSteps(num))

