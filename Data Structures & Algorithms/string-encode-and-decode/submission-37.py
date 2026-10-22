class Solution:

    delimiter = "%"

    def encode(self, strs: List[str]) -> str:

        encoded = ""
        for s in strs:
            encoded = encoded + str(len(s)) + self.delimiter + s
        
        return encoded

        


    def decode(self, s: str) -> List[str]:

        decoded = []

        i = 0
        while i < len(s):

            length = ""
            while s[i] != self.delimiter:
                length += s[i]
                i += 1
            
            length = int(length)
            i += 1
            end = i + length
            extracted = s[i:end]
            decoded.append(extracted)
            i += length
        
        return decoded

                

# cat, elephant, bird, hello my name is
# 3%cat8%elephant4%bird16%hello my name is

# encode
# join the strings
# unique delimiter
# decode that recognizes the delimiter
