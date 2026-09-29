from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq=defaultdict(list)
        for pre, course in prerequisites:
            prereq[pre].append(course)

        visit=set()
        finished=set()
        for i in range(numCourses):
            if i not in finished:
                if not self.dfs(i,visit,finished,prereq):
                    return False
        
        return True

    def dfs(self,pre,visit,finished,prereq):
        if pre in visit:
            return False
        if pre in finished:
            return True 
        visit.add(pre)
        for course in prereq[pre]:
            if not self.dfs(course,visit,finished,prereq):
                return False 
        visit.remove(pre)
        finished.add(pre)
        return True
