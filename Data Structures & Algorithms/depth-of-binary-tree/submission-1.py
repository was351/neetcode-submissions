# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.depth(root,0)
    
    def depth(self,node,count):
        if node is None:
            return count
        l_depth=self.depth(node.left,count + 1)
        
        r_depth=self.depth(node.right,count + 1)
        
        return max(r_depth,l_depth)
        
