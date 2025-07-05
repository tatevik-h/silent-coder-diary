class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        total_sum = 0
        start = 0
        prefix_sum= []
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            prefix_sum.append(prefix)

        for i in range(len(nums)):
            start = max(0, i - nums[i])
            total_sum += prefix_sum[i]

            if start > 0:
                total_sum -= prefix_sum[start-1]

        return total_sum
      
