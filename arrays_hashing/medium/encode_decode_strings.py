# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.
# Please implement encode and decode
# Example 1: 
# Input: ["neet","code","love","you"]
# Output:["neet","code","love","you"]

class Solution:

    def encode(self, strs: list[str]) -> str:
        finalString = ""
        for i, str in enumerate(strs):
            finalString += "{}#{}".format(len(str), str)
        return finalString

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res