# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.traverse(root, 0)

    def traverse(self, root, depth):
        if not root:
            return depth

        depth += 1
        left = self.traverse(root.left, depth)
        right = self.traverse(root.right, depth)

        return max(left, right)
