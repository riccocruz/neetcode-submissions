# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def helper(n):
            if not n:
                return
            res.append(n.val)
            helper(n.left)
            helper(n.right) 

        helper(root)
        return res