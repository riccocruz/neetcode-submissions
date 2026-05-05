# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True

        def helper(n):
            if not n:
                return 0
            
            nonlocal res
            left = helper(n.left)
            right = helper(n.right)

            if abs(left - right) > 1:
                res = False
            
            return 1 + max(left, right)
        
        helper(root)
        return res