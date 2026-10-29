class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, total, sum_arr):
            if total == target:
                res.append(sum_arr.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            sum_arr.append(nums[i])
            total += nums[i]
            dfs(i, total, sum_arr)
            sum_arr.pop()
            total -= nums[i]
            dfs(i + 1, total, sum_arr)
        
        dfs(0, 0, [])
        return res
