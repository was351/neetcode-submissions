# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.post(root)
    def post(self,node,arr=None):
        if arr is None:
            arr=[]
        if node is None:
            return arr
        self.post(node.left,arr)
        self.post(node.right,arr)
        arr.append(node.val)
        return arr
