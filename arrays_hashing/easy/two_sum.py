# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
# Return the answer with the smaller index first.
# Example 1:
# Input: 
# nums = [3,4,5,6], target = 7
# Output: [0,1]

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        visited_nums = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in visited_nums:
                return [visited_nums[diff], i]
            visited_nums[num] = i
        return []