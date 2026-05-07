"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        res=[]
        visit=set()
        clone={}

        return self.dfs(node,visit,clone)
        

    def dfs(self,node,visit,clone):
        if not node:
            return 
        if node in clone:
            return clone[node]
        new=Node(node.val)
        clone[node]=new
        if node.neighbors:
            for val in node.neighbors:
                new.neighbors.append(self.dfs(val,visit,clone)) 
                  
        return new