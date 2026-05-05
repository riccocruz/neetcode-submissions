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
            nonlocal res
            if not res:
                return res

            if not n:
                return True
            
            left = helper(n.left)
            right = helper(n.right)
            res = res and abs(left - right) <= 1
            return 1 + max(left, right)
        helper(root)
        return res
            