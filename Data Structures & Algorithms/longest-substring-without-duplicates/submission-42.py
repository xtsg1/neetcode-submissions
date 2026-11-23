# rep nov 23

# QUESTION
# longest substring with no dupes

# APPROACH
# this is a sliding window question
# window must dynamically expand contract depending on truth condition
# which is whether whats within the window has dupes or not
# how to check for dupes withint he window
# as the window grows add to a set
# if new candidate to add in right pointer r is already in set
# then the left pointers item has to be removed from that window set
# keep track of longest ever seen

# time: window slides once O(n)
# space: even with a set it could be as big as s in theory so O(n)

# walkthrough
# a _ b _ c _ d
#     l
#       r

# window: b
# longest: 3


# solved: 12:30
# i initially thought it was an off by one error, but i manual traced and i found out that i used an if instead of while
# what this did is only contract l by one but the logic amiss was that simply decrementing the leftmost char doesn't guarantee the dupe is removed
# only by removinig all leftmost characters until the window is valid again will work


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:


        l = 0
        r = 0
        longest = 0
        window = set()

        while r < len(s):

            while s[r] in window:  #what i thought was an off-by-one error, actually was because i initially wrote if isntead of while, l pointer must contract until NO dupes are left in window
                window.remove(s[l])
                l += 1
            
            window.add(s[r])
            length = len(window)
            longest = max(longest, length)
            r += 1
        
        return longest
            

            
            




        