class Solution:
    def longestPalindrome(self, s: str) -> str:
        a = ""
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                b = s[i:j]
                if b == b[::-1] and len(b) > len(a):
                    a = b
        return a