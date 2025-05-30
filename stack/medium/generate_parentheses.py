"""
You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.
Example 1:
Input: n = 1
Output: ["()"]
Example 2:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
"""
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res