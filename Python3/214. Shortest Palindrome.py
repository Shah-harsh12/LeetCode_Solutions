class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        rev = s[::-1]
        new_str = s + "#" + rev
        
        lps = [0] * len(new_str)
        length = 0
        
        for i in range(1, len(new_str)):
            while length > 0 and new_str[i] != new_str[length]:
                length = lps[length - 1]
            
            if new_str[i] == new_str[length]:
                length += 1
                lps[i] = length
        
        pal_len = lps[-1]
        
        return rev[:len(s) - pal_len] + s
        