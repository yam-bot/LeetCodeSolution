class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        #for i in range(len(height)):
        #    r = len(height) -1
        #    while i < r:
        #        area = min(height[i],height[r]) * (r-i)
        #        maxarea = max(area,maxarea)
        #        r -= 1
        #return maxarea
        l, r = 0, len(height)-1
        while l < r:
            area = min(height[l],height[r]) * (r-l)
            maxarea = max(area,maxarea)
            if height[l] > height[r]:
                r -= 1
            elif height[r] >= height[l]:
                l += 1
        return maxarea