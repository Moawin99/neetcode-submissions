class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        counter = 0
        arr = []
        while counter < 2:
            for i in range(len(nums)):
                if counter == 2:
                    arr.append(nums[i + len(nums)])
                else:
                    arr.append(nums[i])
            counter += 1
        return arr
