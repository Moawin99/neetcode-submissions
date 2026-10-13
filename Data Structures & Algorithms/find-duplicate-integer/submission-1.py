class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hm = set()
        for x in nums:
            if x in hm:
                return x
            else:
                hm.add(x)
        