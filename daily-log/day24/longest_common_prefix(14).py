class Solution:
    def is_common_prefix(strs, length):
        prefix = strs[0][:length]
        for s in strs[1:]:
            if not s.startswith(prefix):
                return False
        return True

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
    
        min_len = min(len(s) for s in strs)
        low, high = 0, min_len

        while low < high:
            mid = (low + high + 1) // 2
            if Solution.is_common_prefix(strs, mid):
                low = mid
            else:
                high = mid - 1

        return strs[0][:low]
      
