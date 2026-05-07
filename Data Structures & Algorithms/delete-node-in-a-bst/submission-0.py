# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        root=self.rem(root,key)
        return root 
    def rem(self,node,val):
        if not node:
            return None
        if node.val == val:
            if not node.right:
                return node.left
            elif not node.left:
                return node.right
            else:
                node.val=self.find_min(node.right)
                node.right=self.rem(node.right,node.val)
        elif node.val>val:
             node.left=self.rem(node.left,val)
        else:
            node.right=self.rem(node.right,val)
        return node 

    def find_min(self,node):
        if node:
            cur=node
        while cur and cur.left:
            cur=cur.left 
        return cur.val
        