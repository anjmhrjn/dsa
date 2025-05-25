# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
# Each product is guaranteed to fit in a 32-bit integer.
# Follow-up: Could you solve it in O(n) time without using the division operation?
# Example 1: 
# Input: nums = [1,2,4,6] 
# Output: [48,24,12,8]

# Extra space
class SolutionWithExtraSpace:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        pre = [1] * len(nums)
        post = [1] * len(nums)
        for i in range(1, len(nums)):
            pre[i] = pre[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            post[i] = post[i+1] * nums[i+1]
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = pre[i] * post[i]
        return res
    
# less space
class SolutionWithLessSpace:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * (len(nums))

        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
