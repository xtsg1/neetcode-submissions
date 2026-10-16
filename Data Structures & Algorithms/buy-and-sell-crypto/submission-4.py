
#optimization
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_seen = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_seen:
                min_seen = price
            if price - min_seen > max_profit:
                max_profit = price - min_seen

        return max_profit




# O(n^2) because double loop
                



# 1 5 3 6 4 7
#   i
#     j
        