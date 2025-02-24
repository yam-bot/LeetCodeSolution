# 0 -- 1 -- 3
#   \     /
#      2
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {i : [] for i in range(numCourses)}
        for c,p in prerequisites:
            prereq[c].append(p)
        ans,visited, cycle = [], set() , set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            cycle.add(crs)
            for p in prereq[crs]:
                if dfs(p) == False:
                    return False
            cycle.remove(crs)
            visited.add(crs)
            ans.append(crs)
            return True
        for i in range(numCourses):
            if dfs(i) == False:
                return []
        return ans
            