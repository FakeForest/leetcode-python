# LeetCode 347 - Top K Frequent Elements
# Time: O(n + u log u) average
# Space: O(u)

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        ranked = sorted(
            counts.items(),
            key=lambda x: x[1],
            reverse=True
        )
        return [num for num, freq in ranked[:k]]
