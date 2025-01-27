class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        matrix = [[False] * numCourses  for i in range(numCourses)]
        for p in prerequisites :
            matrix[p[0]][p[1]] = True
        for i in range(numCourses):
            for j in range(numCourses):
                for k in range(numCourses):
                    if matrix[j][k] or (matrix[j][i] and matrix[i][k]):
                        matrix[j][k] = True
        return [matrix[q[0]][q[1]]for q in queries]