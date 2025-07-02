class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_prefix = 0
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            min_prefix = min(min_prefix, prefix_sum)

        return max(1 - min_prefix, 0)
      
