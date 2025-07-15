class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m_c = Counter(magazine)
        for i in range(len(ransomNote)):
            if ransomNote[i] not in m_c or m_c[ransomNote[i]] < 1:
                return False
            else:
                m_c[ransomNote[i]] -= 1 
        return True
      
