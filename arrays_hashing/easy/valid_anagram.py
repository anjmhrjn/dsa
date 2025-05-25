# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
# Example 1:
# Input: s = "racecar", t = "carrace"
# Output: true

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            first_dict = {}
            second_dict = {}
            for i in range(len(s)):
                first_dict[s[i]] = 1 + first_dict.get(s[i], 0)
                second_dict[t[i]] = 1 + second_dict.get(t[i], 0)
            return first_dict == second_dict


        