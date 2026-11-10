# rep nov 10

# APPROACH
# we're going to use the length of each string plus a delimieter to encode
# to decode we will read the length up until the delimiter
# use a pointer thats flexible
# then read in the string all at once
# and append to a growing list

# WALKTHROUGH

# hello, world, thisisaverylongstring
# 5%hello5%world21%thisisaverylongstring
#   2    7
#        i

# length 5
# start 2 
# end 7
# word slice: hello 


class Solution:

    
    def encode(self, strs: List[str]) -> str:

        delim = "%"

        encoded = ""
        for s in strs:
            encoded = encoded + str(len(s)) + delim + s
        
        print(encoded)
        return encoded




    def decode(self, s: str) -> List[str]:
        
        delim = "%"

        decoded = []
        i = 0
        while i < len(s):

            length = "" 
            while s[i] != delim:
                length = length + s[i]
                i += 1
            
            length = int(length) #str to int
            start = i + 1
            end = start + length
            word = s[start:end]
            decoded.append(word)
            i = end

        return decoded 
