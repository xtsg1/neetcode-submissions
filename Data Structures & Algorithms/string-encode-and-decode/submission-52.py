# rep Nov 3rd

# QUE
# encode -> decode -> output exact same string
# list -> str -> list

# APPROACH
# trick is to use the length of the word
# and then a delimiter
# as you're looping thorugh loop until delimiter (that gives you the length on decode)

# STEPTHRU
# hello world 
# 5%hello5%world 

# still stuggled and needed some minor hints took full 25 minutes
# but got called away for oncall incident halfway through so disrupted context


class Solution:

    delimiter = '%'

    def encode(self, strs: List[str]) -> str:

        encoded = ""
        for s in strs:
            length = str(len(s))
            encoded = encoded + length + self.delimiter + s
        
        return encoded

# 5%hello
#  i

    def decode(self, s: str) -> List[str]:

        decoded = []

        i = 0
        while i < len(s):

            length =  ""
            while s[i] != self.delimiter:
                length = length + s[i]
                i += 1

            length = int(length)
            start = i + 1
            end = i + length + 1
            word = s[start:end]
            decoded.append(word)
            i = end
        
        return decoded

            
            
                

            


