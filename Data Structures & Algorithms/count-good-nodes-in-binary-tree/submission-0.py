# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count=0
        self.recurse(root,root.val)
        return self.count
    def recurse(self,node,high):
        if not node:
            return 
        elif node.val>= high:
            self.count+=1
            high=node.val
        self.recurse(node.left,high)
        self.recurse(node.right,high)
        return
        