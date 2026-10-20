
#rep oct 20

class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        paired_strings = []  # anagram,original
        for s in strs:
             anagram = "".join(sorted(s))
             original_anagram_pair = (anagram, s)
             paired_strings.append(original_anagram_pair)
        
        grouped_strings = {}
        for t in paired_strings:
            if t[0] not in grouped_strings:
                grouped_strings[t[0]] = [t[1]]
            else:
                grouped_strings[t[0]].append(t[1])

        res = []
        for v in grouped_strings.values():
            res.append(v)
        return res





# loop through strings
# create count dictionary for each string
        
#['act', 'opst', 'opst', 'act', 'opst', 'aht']