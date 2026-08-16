import math
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        a = math.isqrt(num)
        if a * a == num:
            return True
        else:
            return False