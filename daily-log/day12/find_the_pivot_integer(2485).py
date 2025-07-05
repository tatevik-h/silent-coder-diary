class Solution:
    def pivotInteger(self, n: int) -> int:
        prefix = [0] * (n + 2)  

        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + i

        for x in range(1, n + 1):
            left = prefix[x]        
            right = prefix[n] - prefix[x - 1]
            if left == right:
                return x

        return -1
      
