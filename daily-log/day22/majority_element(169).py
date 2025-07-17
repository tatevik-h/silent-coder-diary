class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        distinct_nums = set(nums)
        count = len(nums) // 2
        for elem in distinct_nums:
            if nums.count(elem) > count:
                return elem
        
