# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=deque()
        master=[]
        if root:
            queue.append(root)
        while queue:
            templen=len(queue)
            counter=0
            layer=[]
            while counter<templen:
                cur=queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                    
                if cur.right:
                    queue.append(cur.right)
                counter += 1
                layer.append(cur.val)
            master.append(layer)
        return master
