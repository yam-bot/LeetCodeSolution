class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x = sorted(rectangles)
        y = sorted(rectangles, key = lambda x : x[1])
        prev_endx, prev_endy, divx, divy = 0, 0, 0, 0
        for i in range(len(rectangles)):
            startx, endx, starty, endy = x[i][0] ,x[i][2], y[i][1], y[i][3]
            newstartx = max(prev_endx,startx)
            newstarty = max(prev_endy,starty)
            if newstartx == startx:
                divx += 1
            if newstarty == starty:
                divy += 1
            prev_endx = max(prev_endx,endx)
            prev_endy = max(prev_endy,endy)
        if divx > 2 or divy > 2:
            return True
        else:
            return False

