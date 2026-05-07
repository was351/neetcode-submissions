# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root:
            return self.rec(root,-float('inf'),float('inf'))
    def rec(self,node,min,max):
        if node is None:
            return True
        if node.val>min and node.val<max:
            return self.rec(node.left,min,node.val) and self.rec(node.right,node.val,max)
        return False 
        