# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue=deque()
        right=[]
        counter=0
        if root:
            queue.append(root)
            cur=root
        while queue:
            layer=len(queue)
            for i in range(layer):
                cur=queue.popleft()
                if counter+1==layer:
                    right.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                counter+=1
            counter=0
        return right
            
                



        return right 