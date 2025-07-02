class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_h = 0
        prefix_sum = 0
        for i in range(len(gain)):
            prefix_sum += gain[i]
            max_h = max(prefix_sum, max_h)
        
        return max_h
        
