"""
You are given an array of integers nums and an integer k. There is a sliding window of size k that starts at the left edge of the array. The window slides one position to the right until it reaches the right edge of the array.
Return a list that contains the maximum element in the window at each step.
Example 1:
Input: nums = [1,2,1,0,4,2,6], k = 3
Output: [2,2,4,4,6]
Explanation: 
Window position            Max
---------------           -----
[1  2  1] 0  4  2  6        2
 1 [2  1  0] 4  2  6        2
 1  2 [1  0  4] 2  6        4
 1  2  1 [0  4  2] 6        4
 1  2  1  0 [4  2  6]       6
"""

import collections
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        output = []
        l = r = 0
        q = collections.deque()

        while r < len(nums):
            while q and [q-1] < nums[r]:
                q.pop()
            q.append(r)
            
            if l > q[0]:
                q.popleft()

            if r + 1 >= k:
                output.append(nums[q[0]])
                l += 1
            
            r += 1
        return output