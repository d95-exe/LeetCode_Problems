class Solution:
    def maximumWealth(self, accounts) -> int:
        sums = []
        for i in range(len(accounts)):
            total = 0
            for j in range(len(accounts[0])):
                total += accounts[i][j]
            sums.append(total)
        return max(sums)

sol = Solution()

accounts = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
print(sol.maximumWealth(accounts))

