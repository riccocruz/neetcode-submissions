# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        # I could not explain this properly. Do it again
        # and explain it step by step.
        def dfs(n):
            if not n:
                return 0
            
            nonlocal res

            left = dfs(n.left)
            right = dfs(n.right)
            res = max(res, left + right)
            return 1 + max(left, right)
        dfs(root)
        return res