class Solution:
    def singleNumber(self, nums: List[int]) -> int:
            cavab = 0
            for reqem in nums:
                cavab ^= reqem
            return cavab