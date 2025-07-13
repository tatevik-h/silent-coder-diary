class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water = 0
        
        for i, h in enumerate(height):
            while stack and height[i] > height[stack[-1]]:
                bottom = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                width = i - left - 1
                max_baund = min(height[left], height[i]) - height[bottom]
                water += width * max_baund

            stack.append(i)

        return water
