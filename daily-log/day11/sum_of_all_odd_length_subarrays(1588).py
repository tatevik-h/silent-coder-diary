class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        prefix_sum = [arr[0]]
        sum_arr = 0
        for elem in arr[1:]:
            prefix_sum.append(prefix_sum[-1]+elem)

        for i in range(1, len(arr)+ 1, 2):
            sum_arr += sum(prefix_sum[-i:]) - sum(prefix_sum[:i -1 ])
            print(sum_arr)

        return sum_arr
