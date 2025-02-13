class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        maxCandy = max(candies)
        return [candy + extraCandies >= maxCandy for candy in candies]
