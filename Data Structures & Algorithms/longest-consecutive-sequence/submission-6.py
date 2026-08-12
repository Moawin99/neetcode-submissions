class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        count_map = {} 
        sort = sorted(nums)
        for x in sort:
            if x in count_map:
                continue
            elif x - 1 in count_map:
                count_map[x] = count_map.get(x-1) + 1
            else:
                count_map[x] = 1
        return max(count_map.values())
       
