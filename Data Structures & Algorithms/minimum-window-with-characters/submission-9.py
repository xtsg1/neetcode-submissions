# todo fix this shit
class Solution:

    def minWindow(self, s: str, t: str) -> str:

        t_count = {}
        for c in t:
            t_count[c] = 1 + t_count.get(c, 0)
        
        required_conditions = len(t_count.keys())
    
        L = 0
        R = 0

        s_count = {}
        conditions_met = 0

        shortest_substring = ""

        while R < len(s):

            s_count[s[R]] = 1 + s_count.get(s[R], 0)

            if s[R] in t_count and s_count[s[R]] == t_count[s[R]]:
                conditions_met += 1
            
            while conditions_met == required_conditions:  #valid substring

                if not shortest_substring:
                    shortest_substring = s[L:R+1]

                if (R + 1 - L) < len(shortest_substring):
                    shortest_substring = s[L:R+1]

                s_count[s[L]] -= 1  
                if s[L] in t_count and s_count[s[L]] == t_count[s[L]] - 1:
                    conditions_met -= 1
                L += 1

            R += 1
            
        
        return shortest_substring


# O U Z O D Y X A Z V
# L       
# R
        

        



# s and t
# shortest substring of s that has ever letter of t
# must include duplicates
# order doesn't matter

# count dictionary for t
# sliding window in s
# valid condition is containing all elements of t
# dynamically generate s dict
# check equivalent to t
# slide if not equivalent
        