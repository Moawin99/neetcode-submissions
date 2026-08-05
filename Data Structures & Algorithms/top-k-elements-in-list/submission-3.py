class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = {}
        for x in nums:
            if x not in my_map:
                my_map[x] = 0
            my_map[x] = my_map[x] + 1
        maxes = sorted(my_map.values(), reverse=True)
        values = [maxes[x] for x in range(k)]
        print(values)
        ans = []
        for x in values:
            for y in list(my_map.keys()):
                if my_map[y] == x:
                    ans.append(y)
                    del my_map[y]
                    break
        return ans