# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def helper(n):
            if not n:
                return
            
            helper(n.left)
            helper(n.right)
            res.append(n.val)
        
        helper(root)
        return res