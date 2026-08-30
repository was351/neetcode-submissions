# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True 
        else:
            left=self.depth(root.left)
            right=self.depth(root.right)
            if  abs(right-left) <=1 :
                return True
            else:
                return False
    def depth(self,root):
        if not root:
            return 0
        left=1+self.depth(root.left)
        right=1+self.depth(root.right)
        return max(left,right)

        
            

        
    
