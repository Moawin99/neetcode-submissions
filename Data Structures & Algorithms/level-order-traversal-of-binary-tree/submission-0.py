# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def dfs(root, h):
            if not root:
                return 
            if len(res) == h:
                res.append([])
            
            res[h].append(root.val)
            dfs(root.left, h +1)
            dfs(root.right, h +1)
            return
        dfs(root, 0)
        return res