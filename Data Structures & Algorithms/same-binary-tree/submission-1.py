# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def helper(a, b):
            if not a and not b:
                return True
            
            if a and b and a.val == b.val:
                return helper(a.left, b.left) and helper(a.right, b.right)
            return False
        
        return helper(p, q)