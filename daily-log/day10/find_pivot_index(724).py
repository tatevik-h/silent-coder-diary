class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum = 0
        rightsum = sum(nums)

        for i in range(len(nums)):
            rightsum -= nums[i]
            if abs(rightsum - leftsum) == 0:
                return i
            leftsum += nums[i]

        return -1
        
