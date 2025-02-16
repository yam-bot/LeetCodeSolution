class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n , stack = len(nums) , []
        res = [-1] * n
        right = [-1] * n
        left = [-1] * n
        circularIndex = []
        count = 2
        while count > 0:
            for i in range(n-1,-1,-1):
                i = i  % n
                circularIndex.append(i)
            count -= 1
        #for j in range(n-1,-1,-1):
        #print(circularIndex)
        for i in circularIndex:
            while stack and nums[i] >= nums[stack[-1]] :
                stack.pop()
            res[i] = nums[stack[-1]] if stack else -1
            stack.append(i)
            #print(nums[i],"right",right,"stack",stack)
        return res
# 1 2 1