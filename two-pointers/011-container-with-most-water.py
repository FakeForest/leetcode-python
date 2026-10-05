# LeetCode 11 - Container With Most Water
# Time: O(n)
# Space: O(1)


class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            current = (right - left) * min(height[left], height[right])

            if current > max_area:
                max_area = current

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
