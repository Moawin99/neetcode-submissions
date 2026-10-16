# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.hm = {}
        self.res = TreeNode(-101)
        
        def dfs(root, p, q):
            if not root:
                return []
            
            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)
            self.hm[root] = self.hm.get(root, []) + [root] + left + right

            cur = self.hm.get(root, [])
            
            if p in cur and q in cur and self.res.val == -101:
                print(root.val)
                self.res = root

            return self.hm[root]
        
        dfs(root, p, q)
        return self.res

        