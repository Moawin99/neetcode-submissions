class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def dfs(i, total, sum_arr):
            if total == target and sorted(sum_arr) not in res:
                res.append(sum_arr.copy())
                return 
            if total > target or i == len(candidates):
                return
            
            sum_arr.append(candidates[i])
            total += candidates[i]
            dfs(i + 1, total, sum_arr)
            sum_arr.pop()

            total -= candidates[i]
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, total, sum_arr)
        
        dfs(0, 0, [])
        return res