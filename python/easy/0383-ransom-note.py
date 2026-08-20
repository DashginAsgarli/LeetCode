class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = ''
        for i in ransomNote:
            if i in magazine:
                a += i
                magazine = magazine.replace(i, "", 1)
        
        if a == ransomNote:
            return True
        else:
            return False