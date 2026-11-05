# rep nov 5

# QUESTION
# buy on a day
# sell day after buy day
# whats the max profit

# APPROACH
# keep track of lowest ever seen
# keep track of highest ever seen



class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        most_profit = 0 
        lowest = prices[0]
        for p in prices:

            if p > lowest:
                profit = p - lowest 
                most_profit = max(most_profit, profit)
            
            lowest = min(lowest, p)
        
        return most_profit
        