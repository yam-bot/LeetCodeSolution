class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        source, res = [], []
        visited = set()
        rowlen, colen = len(isWater) , len(isWater[0])
        queue = deque()
        for i,r in enumerate(isWater):
            for j,c in enumerate(r):
                if c == 1:
                    isWater[i][j] = 0
                    visited.add((i,j))
                    queue.append((i,j,0))
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        while queue:
            #print(queue," res: ",isWater," visited: ",visited)
            r,c,height = queue.popleft()
            if (r,c) not in visited:
                visited.add((r,c))
            #print(visited)
            for dr, dc in direction:
                nr , nc = r + dr, c + dc
                #print("nr",nr,"nc",nc,"visited",visited)
                if 0 <= nr and nr < rowlen and 0 <= nc and nc < colen and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    isWater[nr][nc] = height + 1
                    queue.append((nr,nc,height+1))
            #print(queue)
        return isWater
