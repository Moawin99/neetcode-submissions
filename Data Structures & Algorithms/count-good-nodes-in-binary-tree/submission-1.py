# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, float('-inf'))

    def dfs(self, root, curMax):
        if not root:
            return 0

        if root.val < curMax:
            return self.dfs(root.left, curMax) + self.dfs(root.right, curMax)
        else:
            return 1 + self.dfs(root.left, max(curMax, root.val)) + self.dfs(root.right, max(curMax, root.val))