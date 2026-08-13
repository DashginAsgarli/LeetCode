class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_str = "".join([str(i) for i in digits])
        l3_str = str(int(digits_str) + 1)
        l3 = [int(i) for i in l3_str]
        return l3