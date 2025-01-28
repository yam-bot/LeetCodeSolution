class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rowlen , colen = len(grid) , len(grid[0])
        maxfish = 0
        currfish = 0
        visited = set()
        def dfs(r,c):
            nonlocal currfish
            if grid[r][c] == 0 :
                print("no fish")
                return
            else:
                direction = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
                for currow, currcol in direction:
                    if 0 <= currow < rowlen and 0 <= currcol < colen and (currow,currcol) not in visited:
                        print("( ",currow, currcol," )")
                        currfish += grid[currow][currcol]
                        visited.add((currow,currcol))
                        dfs(currow,currcol)
            return 
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col > 0 :
                    print("initiate : ", "( ",i,j," )")
                    currfish = col
                    visited.add((i,j))
                    dfs(i,j)
                    maxfish = max(maxfish,currfish)
        return maxfish

