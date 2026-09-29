# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    longest=0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.depth(root)
        return self.longest
    
    def depth(self,node):
        if not node:
            return 0
        left=self.depth(node.left)
        right=self.depth(node.right)
        self.longest=max(self.longest,right+left)
        return 1+max(left,right)

        