class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for x in nums:
            count[x] = count.get(x, 0) + 1
        
        max_sorted = (sorted(count.values())[::-1])[:k]

        most = []

        for x in nums:
            if count[x] in max_sorted and x not in most:
                most.append(x)
        
        return most