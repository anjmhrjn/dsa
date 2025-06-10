"""
Given an unsorted array of integers nums and an integer k, return the kth largest element in the array.
By kth largest element, we mean the kth largest element in the sorted order, not the kth distinct element.
Follow-up: Can you solve it without sorting?
Example 1:
Input: nums = [2,3,1,5,4], k = 2
Output: 4
"""
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # sorted approach
        # nums.sort()
        # return nums[len(nums) - k]

        # quick select approach
        k = len(nums) - k

        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k:
                return quickSelect(l, p - 1)
            elif p < k:
                return quickSelect(p+1, r)
            else:
                return nums[p]
        
        return quickSelect(0, len(nums) - 1)
            