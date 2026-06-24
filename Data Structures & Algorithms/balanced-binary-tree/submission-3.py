# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def postorder(n):
            nonlocal res
            if not n or not res:
                return 0
            left = postorder(n.left)
            right = postorder(n.right)
            if not res:
                return 0
            res = abs(left - right) <= 1

            return 1 + max(left, right)
        
        postorder(root)
        return res