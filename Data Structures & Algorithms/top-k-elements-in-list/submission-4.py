class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = {}
        for x in nums:
            my_map[x] = my_map.get(x, 0) + 1
        counts = [[] for i in range(len(nums) + 1)]
        for key, value in my_map.items():
            counts[value].append(key)
        ans = []
        for i in range(len(counts) - 1, 0, -1):
            for y in counts[i]:
                ans.append(y)
                if len(ans) == k:
                    return ans
# Bucket Sort
# HashMap to count occurances