# exam nov 28

# QUESTION
# max profit
# can buy and sell as many times

# APPROACH
# as long as its ascending its profitable
# but if descends it makes more sense to sell at the high, rebuy at low then keep going
# if it never recovers then dont buy this is the end case
# so i think this is more of a two pointer approach
# one pointer on the buy date, one pointer keeps going as long as prices are going up
# if prices are dropping we close the trade, book the profits
# move the left pointer up and scan again so its kind of a window function
# if descending we skip
# we need something to store state like profitable

# RUNTIME: O(n) for to scan through all elements once
# MEMORY: O(1) for pointers + profit

# WALK
# 7 1 5 3 6 4
#   b  
#     s  

# total 40m coudl not solve it cold fml

class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        # buy/sell pointers
        b = 0
        s = 0

        cumulative_profit = 0
        profit = 0

        while s < len(prices):

            if prices[s] < prices[s-1]:
                if profit: #take profits
                    cumulative_profit += profit # 0+4
                    profit = 0
                b = s
                s += 1
                continue
            
            if prices[s] > prices[b]:
                profit = prices[s] - prices[b]  #5-1 = 4
            
            s += 1
        
        return cumulative_profit + profit

            

