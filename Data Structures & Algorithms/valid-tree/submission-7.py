from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        branches=defaultdict(list)
        for node,edge in edges:
            branches[node].append(edge)
            branches[edge].append(node)
        visit=set()
        finished=set()
        if not self.dfs(0,-1,visit,finished,branches):
            return False
            
        return len(visit)==n
    def dfs(self,i,parent,visit,finished,branches):
        if i in visit:
            return False
        visit.add(i)
        for node in branches[i]:
            if node in visit:
                if node !=parent:
                    return False
            else:
                if not self.dfs(node,i,visit,finished,branches):
                    return False
        
        return True
        