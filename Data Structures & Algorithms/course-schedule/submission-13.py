from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs=defaultdict(list)
        for course,pre in prerequisites:
            prereqs[course].append(pre)
        visit=set()
        finished=set()
        for i in range(numCourses):
        
            if not self.dfs(i,visit,finished,prereqs):
                return False
                
        return True 


    def dfs(self,i,visit,finished,prereq):
        if i in visit:
            return False 
        if i in finished:
            return True 
        visit.add(i)
        for req in prereq[i]:
            if req in visit:
                return False
            else:
                if not self.dfs(req,visit,finished,prereq):
                    return False 
        visit.remove(i)
        finished.add(i)
        return True 
        





        