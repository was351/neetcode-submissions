# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            new=TreeNode(val)
            return new
        self.insert(root,val)
        return root
    def insert(self,node,val):
        if node.val>val:
            if not node.left:
                new=TreeNode(val)
                node.left=new
                return
            self.insert(node.left,val)
        if node.val<val:
            if not node.right:
                new=TreeNode(val)
                node.right=new
                return
            self.insert(node.right,val)