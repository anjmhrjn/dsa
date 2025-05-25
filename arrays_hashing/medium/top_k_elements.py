# Given an integer array nums and an integer k, return the k most frequent elements within the array.
# The test cases are generated such that the answer is always unique.
# You may return the output in any order.
# Example 1:
# Input: nums = [1,2,2,3,3,3], k = 2
# Output: [2,3]

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = [[] for i in range(len(nums) + 1)]
        num_count = {}
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
        for n, c in num_count.items():
            freq[c].append(n)
        freq_values = []
        for i in range(len(freq)-1, 0, -1):
            for j in freq[i]:
                freq_values.append(j)
                if len(freq_values) == k:
                    return freq_values