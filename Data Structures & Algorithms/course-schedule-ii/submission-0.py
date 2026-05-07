from collections import defaultdict
class Solution:

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre=defaultdict(list)
        for u,v in prerequisites:
            pre[v].append(u)
        visit=set()
        path=set()
        valid=[]
        cur=[]
        for i in range(numCourses):
            if not self.dfs(i,path,visit,cur,pre):
                return []  
        cur.reverse()
        return cur

    
    def dfs(self,node,path,visit,cur,pre):
        if node in path:
            return False
        if node in visit:
            return True
        path.add(node)
        for val in pre[node]:
            if not self.dfs(val,path,visit,cur,pre):
                return False
        path.remove(node)
        visit.add(node)
        cur.append(node)
        return True
            
        