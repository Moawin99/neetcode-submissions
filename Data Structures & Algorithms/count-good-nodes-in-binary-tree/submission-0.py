# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = []
        stack = []

        def dfs(root):
            if not root:
                return root

            stack.append(root.val)

            dfs(root.left)
            dfs(root.right)

            node = stack.pop()
            sLen = len(stack)

            if stack:
                for i in range(sLen):
                    if node < stack[i]:
                        return root
            
            res.append(node)

        dfs(root)
        return len(res)