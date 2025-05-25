# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
# Example 1:
# Input: strs = ["act","pots","tops","cat","stop","hat"]
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

class Solution:
    def isAnagram(self, s: str, t: str):
        if (len(s) != len(t)):
            return False
        sCount = {}
        tCount = {}
        for i in range(len(s)):
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
            tCount[t[i]] = 1 + tCount.get(t[i], 0)
        return sCount == tCount

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = []
        visited_indices = set()
        for i in range(0, len(strs)):
            if i not in visited_indices:
                visited_indices.add(i)
                current = [strs[i]]
                counter = 1
                while i + counter < len(strs):
                    if self.isAnagram(strs[i], strs[i+counter]):
                        visited_indices.add(i+counter)
                        current.append(strs[i+counter])
                    counter += 1
                anagrams.append(current)
        return anagrams        