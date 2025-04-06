class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        premax = nums[0]
        res, maxdiff = 0, 0
        for k in range(1,len(nums)):
            res = max(res,maxdiff * nums[k])
            maxdiff = max(maxdiff,premax - nums[k])
            premax = max(premax,nums[k])
        return res
