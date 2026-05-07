# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True 
        return self.find(root,subRoot)
    
    def find(self,node,sub):
        if not node :
            return False 
        if node.val==sub.val:
            if self.isSame(node,sub):
                return True 
        left=self.find(node.left,sub)
        right=self.find(node.right,sub)
        return left or right 
    def isSame(self,node,sub):
        if not node and not sub:
            return True
        if not node and sub or node and not sub:
            return False 
        if node.val != sub.val:
            return False 
        left=self.isSame(node.left,sub.left)
        right=self.isSame(node.right,sub.right)
        return left and right 