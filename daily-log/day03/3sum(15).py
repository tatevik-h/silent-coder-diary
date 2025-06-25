class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)-2):
            if i> 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                s = nums[i] + nums[right] + nums[left]

                if s > 0:
                    right -=1
                elif s < 0:
                    left += 1
                else:
                    triplet = [nums[i], nums[left], nums[right]]
                    if len(result) == 0 or triplet != result[-1]:
                        result.append(triplet)

                    right -= 1
                    left += 1

        return result
