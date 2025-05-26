"""
You are given an integer array heights where heights[i] represents the height of the ith bar.
You may choose any two bars to form a container. Return the maximum amount of water a container can store.
Example 1:
Input: height = [1,7,2,5,4,7,3,6]
Output: 36
"""
class Solution:
    def maxArea(self, heights: list[int]) -> int:
        l, r = 0, len(heights) - 1
        area = 0
        while l < r:
            min_height = min(heights[l], heights[r])
            area = max(area, min_height * (r-l))
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return area
