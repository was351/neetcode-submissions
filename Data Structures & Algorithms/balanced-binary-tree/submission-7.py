# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.rec(root)>=0
    
    def rec(self,node):
        if not node:
            return 0
        
        left=1+self.rec(node.left)
        right=1+self.rec(node.right)
      
        if abs(right-left)>1:
            return -1
        if left==0 or right==0:
            return -1
        return max(left,right)