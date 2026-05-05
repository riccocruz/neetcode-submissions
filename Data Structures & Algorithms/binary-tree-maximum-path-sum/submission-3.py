# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def traverse(n):
            nonlocal res
            if not n:
                return 0
            
            left = traverse(n.left)
            right = traverse(n.right)

            res = max(res, n.val, n.val + left, n.val + right, n.val + left + right)

            return max(n.val, n.val + max(left, right))
        traverse(root)

        return res