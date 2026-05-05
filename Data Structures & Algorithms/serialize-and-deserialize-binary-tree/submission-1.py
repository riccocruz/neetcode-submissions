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
            if all(not n for n in queue):
                break

            l = len(queue)
            for i in range(l):
                n = queue.popleft()

                if n:
                    res.append(str(n.val))
                    queue.append(n.left)
                    queue.append(n.right)
                else:
                    res.append('N')
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None

        data = data.split(",")
        root = TreeNode(int(data[0]))
        queue = deque([root])
        i = 1

        while i < len(data):
            n = queue.popleft()
 
            if data[i] != 'N':
                n.left = TreeNode(int(data[i]))
                queue.append(n.left)
            i += 1
            
            if data[i] != 'N':
                n.right = TreeNode(int(data[i]))
                queue.append(n.right)
            i += 1
            print(i, [n.val for n in queue])
        return root