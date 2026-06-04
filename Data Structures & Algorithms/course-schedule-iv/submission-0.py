from collections import defaultdict 
class Solution:

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        pre=defaultdict(list)
        res=[]
        for i,j in prerequisites:
            pre[i].append(j)
        
        memo = {}

        for i in range(len(queries)):
            start=queries[i][0]
            target=queries[i][1]
            cur=set()
            res.append(self.dfs(start,target,cur,pre, memo))
        return res
    
    def dfs(self,node,target,cur,pre, memo):
        if (node, target) in memo: return memo[(node, target)]
        if node == target:
            return True
        cur.add(node)
        for val in pre[node]:
            if val not in cur:
                if self.dfs(val,target,cur,pre, memo):
                    memo[(node, target)] = True
                    return True 
        memo[(node, target)] = False
        return False