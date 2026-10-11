class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded = encoded + str(len(s)) + "$" + s
        return encoded

    def decode(self, s: str) -> List[str]:

        decoded = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != "$":
                j += 1
            string_length = int(s[i:j])
            start = j + 1
            end = start + string_length
            word = s[start:end]
            i = end
            decoded.append(word)
        
        return decoded
            

#   10$hellopp
#   0123456789
#     j