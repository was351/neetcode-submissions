# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
         return self.depth(root)!=-1

    def depth(self,node):
        if not node:
            return 0
        
        left=self.depth(node.left)
        right=self.depth(node.right)
        if left == -1 or right ==-1:
            return -1 
        if abs(right-left)>1:
            return -1
        
        return 1+max(left,right)