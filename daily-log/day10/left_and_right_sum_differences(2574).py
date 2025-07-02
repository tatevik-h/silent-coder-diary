class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftsum = 0
        rightsum = sum(nums)
        answer = []
        len_num = len(nums)

        for i in range(len_num):

            rightsum -= nums[i]
            answer.append(abs(rightsum - leftsum))
            leftsum += nums[i]

        return answer
        
