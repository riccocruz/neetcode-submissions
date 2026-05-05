# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        # regular traversal, if n.val > key go left. otherwise go right.
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            # root.val == key. first check if no children
            if not root.left and not root.right:
                return None

            # one child:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            
            # two children: find the in order successor of the node:
            # left most of right tree.
            # copy that value then delete that node down there. 
            cur = root.right
            while cur.left:
                cur = cur.left
            root.val = cur.val

            root.right = self.deleteNode(root.right, cur.val)

        return root
