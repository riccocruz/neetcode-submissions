# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same_tree(n, sub):
            if not n and not sub:
                return True
            if n and sub and n.val == sub.val:
                return is_same_tree(n.left, sub.left) and is_same_tree(n.right, sub.right)
            return False
        
        def traverse(n):
            if not n:
                return False
            if n.val == subRoot.val and is_same_tree(n, subRoot):
                return True
            return traverse(n.left) or traverse(n.right)
        
        return traverse(root)
            
        
