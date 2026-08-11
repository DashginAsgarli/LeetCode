class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        long_ch = 0
        a = ''
        
        for i in s:
            if i in a:
                a = a[a.index(i) + 1:]
            
            a += i
            
            if len(a) > long_ch:
                long_ch = len(a)
                
        return long_ch