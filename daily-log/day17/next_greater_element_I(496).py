class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Indx = {val: i for i, val in enumerate(nums1)}
        res = [-1] * len(nums1)
        stack = []

        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                indx = nums1Indx[val]
                res[indx] = cur

            if cur in nums1Indx:
                stack.append(cur)

        return res
        
