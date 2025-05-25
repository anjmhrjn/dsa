# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
# Example 1:
# Input: nums = [1, 2, 3, 3]
# Output: true

class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        newHashset = set()
        for num in nums:
            if num in newHashset:
                return True
            newHashset.add(num)
        return False