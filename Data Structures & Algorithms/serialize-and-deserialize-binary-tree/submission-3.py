# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        res = []
        queue = deque([root])

        while queue:
            n = queue.popleft()
            if n == "N":
                res.append("N")
            else:
                res.append(str(n.val))
                if n.left:
                    queue.append(n.left)
                else:
                    queue.append("N")
                if n.right:
                    queue.append(n.right)
                else:
                    queue.append("N")
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        data = data.split(',')
        root = TreeNode(int(data[0]))
        queue = deque([root])

        i = 0
        while i < len(data) and queue:
            cur = queue.popleft()
            
            i += 1
            if data[i] != 'N':
                cur.left = TreeNode(int(data[i]))
                queue.append(cur.left)
            
            i += 1
            if data[i] != 'N':
                cur.right = TreeNode(int(data[i]))
                queue.append(cur.right)
        return root











