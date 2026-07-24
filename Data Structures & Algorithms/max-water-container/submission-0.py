class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_l = 0

        while left < right:
            diff = right - left
            current = min(heights[right], heights[left]) * diff
            max_l = max(max_l, current)
            if heights[left] < heights[right]:
                left +=1
            else:
                right -= 1
        return max_l