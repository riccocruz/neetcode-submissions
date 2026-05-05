class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest = 0
        buy = float('inf')

        for price in prices:
            buy = min(buy, price)
            highest = max(highest, price - buy)
        return highest