# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        cur_level = [root]
        while cur_level:
            res.append([n.val for n in cur_level])

            children = []
            for n in cur_level:
                if n.left:
                    children.append(n.left)
                if n.right:
                    children.append(n.right)
            
            cur_level = children
        return res