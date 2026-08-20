class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a = ''
        for i in s:
            if i in t:
                a += i
                t = t[t.find(i) + 1:]
        return a == s