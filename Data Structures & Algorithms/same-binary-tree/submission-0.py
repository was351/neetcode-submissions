# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.recurse(p,q)
    def recurse(self,node1,node2):
        if not node1 and not  node2:
            return True
        elif node1 is None:
            return False
        elif node2 is None:
            return False
        elif node1.val != node2.val:
            return False
        return self.recurse(node1.left,node2.left) and self.recurse(node1.right,node2.right)
        
       

        