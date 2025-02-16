class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n , stack = len(nums) , []
        res = [-1] * n
        circularIndex = []
        count = 2
        while count > 0:
            for i in range(n-1,-1,-1):
                i = i  % n
                circularIndex.append(i)
            count -= 1
        for i in circularIndex:
            while stack and nums[i] >= nums[stack[-1]] :
                stack.pop()
            res[i] = nums[stack[-1]] if stack else -1
            stack.append(i)
        return res
