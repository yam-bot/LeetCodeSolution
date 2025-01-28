class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rowlen , colen = len(grid) , len(grid[0])
        maxfish = 0
        visited = set()

        def dfs(r,c):
            if not (0 <= r < rowlen and 0 <= c < colen) or (r,c) in visited or grid[r][c] == 0:
                return 0
            direction = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            visited.add((r,c))
            fish_count = grid[r][c]
            for currow, currcol in direction:
                fish_count += dfs(currow,currcol)
            return fish_count

        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col > 0  and (i,j) not in visited:
                    maxfish = max(maxfish,dfs(i,j))
        return maxfish

