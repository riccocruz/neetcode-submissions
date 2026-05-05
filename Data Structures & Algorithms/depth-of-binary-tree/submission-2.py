# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0

        def helper(n):
            if not n:
                return 0

            nonlocal res
            cur = 1 + max(helper(n.left), helper(n.right))
            res = max(res, cur)
            return cur
        
        helper(root)
        return res