class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        for index, value in enumerate(nums):
            if value not in my_map:
                my_map[value] = []
            my_map[value].append(index)

        for i in range(len(nums)):
            if target - nums[i] in my_map:
                for y in my_map[target - nums[i]]:
                    if i == y:
                        continue
                    return [i, y]