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
        res=[]
        if root:
            queue.append(root)
        while queue:
            count=0
            width=len(queue)
            layer=[]
            while count<width:
                cur=queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                layer.append(cur.val)
                count+=1
            res.append(layer)
            
        return res


