class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_volume = 0
        while left < right:
            width = right - left 
            current_volume = width * min(height[left], height[right])
            max_volume = max(max_volume, current_volume)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_volume
                
        
