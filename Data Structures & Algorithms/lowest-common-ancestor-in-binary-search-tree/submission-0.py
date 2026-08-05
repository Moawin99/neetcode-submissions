# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def search(root, stack, val):
            if root.val == val:
                stack.append(root)
                return stack
            
            stack.append(root)
            if val < root.val:
                search(root.left, stack, val)
            else: 
                search(root.right, stack, val)
            
            return stack
        p_stack = search(root, [], p.val)
        q_stack = search(root, [], q.val)
        while p_stack:
            node = p_stack.pop()
            if node in q_stack:
                return node
        
        return None