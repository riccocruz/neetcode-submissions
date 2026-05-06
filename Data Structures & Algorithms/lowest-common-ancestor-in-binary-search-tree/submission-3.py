# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def helper(n):
            if p.val <= n.val <= q.val or p.val >= n.val >= q.val:
                return n

            if n.val > p.val and n.val > q.val:
                return helper(n.left)
            if n.val < p.val and n.val < q.val:
                return helper(n.right)

        return helper(root)