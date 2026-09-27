# LeetCode 150 - Evaluate Reverse Polish Notation
# Time: O(n)
# Space: O(n)


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
                continue

            right = stack.pop()
            left = stack.pop()
            if token == "+":
                stack.append(left + right)
            elif token == "-":
                stack.append(left - right)
            elif token == "*":
                stack.append(left * right)
            else:
                stack.append(int(left / right))

        return stack[-1]
