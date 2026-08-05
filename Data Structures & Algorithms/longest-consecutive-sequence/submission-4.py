class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == None or len(nums) == 0:
            return 0
        vals = {x: x for x in nums}
        ans_list = []
        lengths = 0

        for key in vals:
            tmp = key
            if (key - 1) not in vals:
                while tmp in vals.keys():
                    lengths += 1
                    tmp += 1
                ans_list.append(lengths)
                lengths = 0
        
        return max(ans_list)