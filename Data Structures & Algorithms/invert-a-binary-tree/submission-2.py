# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(n):
            if not n:
                return
            n.left, n.right = n.right, n.left
            helper(n.left)
            helper(n.right)
        helper(root)
        return root