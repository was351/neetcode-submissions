# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.dfs(root,targetSum)
    def dfs(self,root,target):
        if not root:
            return False
        remain=target-root.val
        if remain==0 and not root.left and not root.right:
            return True
        if not root.left and not root.right:
            return False
        
        if self.dfs(root.left,remain):
            return True
        if self.dfs(root.right,remain):
            return True
        return False