class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        res = 0
        rlen , clen = len(grid) , len(grid[0])
        serverrow = [0] * rlen
        servercol = [0] * clen
        visitedr, visitedc, server = set(), set(), set()
        for i in range(rlen):
            for j in range(clen):
                if grid[i][j] == 1:
                    serverrow[i] += 1
                    servercol[j] += 1
        print(serverrow,servercol)
        for i in range(rlen):
            for j in range(clen):
                if grid[i][j] == 1 and (serverrow[i] > 1 or servercol[j] > 1):
                    res += 1
                    print("( ",i," , ",j," ) ")
        return res
