# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root:
            self.insert_in(root,val)
        else:
            return TreeNode(target)
        return root
        
    
    def insert_in(self,node,target):
        if node.val>target:
            if not node.left:
                node.left=TreeNode(target)
                return
            else:
                self.insert_in(node.left,target)
        if node.val<target:
            if not node.right:
                node.right=TreeNode(target)
                return
            else:
                self.insert_in(node.right,target)
        return

        
