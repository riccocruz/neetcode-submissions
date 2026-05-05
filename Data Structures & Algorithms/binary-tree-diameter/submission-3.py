# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def helper(n):
            if not n:
                return 0

            
            left = helper(n.left)
            right = helper(n.right)

            cur = left + right

            nonlocal res
            res = max(res, cur)
            return 1 + max(left, right)
        
        helper(root)
        return res