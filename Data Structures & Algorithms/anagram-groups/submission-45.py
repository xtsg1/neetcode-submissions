#rep nov 1

## QUESTION
# return list of lists
# each sublist are anagrams of one another


## APPROACH
# a hashmap count would allow anagram comparison
# but sorting string O(n*logn) would also allow anagram comparison
# hashmap is needed for grouping by anagram, not so much for counting characters
# the key is the sorted string
# hashamp keeps tracks of anagram + sublists
# instead of hashmap for counting we just use the sorted string
# loop through every word only once

# time: O(nlogn) in worst case due to sorting
# space: hashmap is required so O(n)
# is O(nlogn) optimal? how do you know whats optimal before you do something?

# WALKTHROUGH
# strs = ["act","pots","tops","cat","stop","hat"]
# s = act
# ordered = act
# [act, cat] 

# {
# "act": ["act", "cat", "tac"],
# "opst": ["pots", "post"]
# }

# finished in 20:03

class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}

        for s in strs:
            akey = "".join(sorted(s))

            if akey not in groups:
                groups[akey] = [s]  #init
            else:
                groups[akey].append(s)

        grouped_anagrams = [] 
        for group in groups.values():
            grouped_anagrams.append(group)
        
        return grouped_anagrams


        



        