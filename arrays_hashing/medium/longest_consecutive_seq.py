"""
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.
You must write an algorithm that runs in O(n) time.
Example 1:
Input: nums = [2,20,4,10,3,4,5]
Output: 4
"""
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        all_nums = set(nums)
        longest = 0
        for num in nums:
            if num-1 not in all_nums:
                length = 1
                while num+length in all_nums:
                    length += 1
                longest = max(length, longest)
        return longest
            
        