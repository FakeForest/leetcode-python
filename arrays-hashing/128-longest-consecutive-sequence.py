# LeetCode 128 - Longest Consecutive Sequence
# Time: O(n) average
# Space: O(n)

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        best = 0

        for num in num_set:
            if num - 1 not in num_set:
                current = num + 1
                while current in num_set:
                    current += 1
                best = max(best, current - num)

        return best
