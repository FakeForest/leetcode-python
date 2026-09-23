# LeetCode 20 - Valid Parentheses
# Time: O(n)
# Space: O(n)


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        for char in s:
            if char in "([{":
                stack.append(char)
            elif not stack or stack[-1] != pairs[char]:
                return False
            else:
                stack.pop()

        return not stack
