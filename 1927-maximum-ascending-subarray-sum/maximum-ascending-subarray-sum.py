class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        l , currsum , maxsum = len(nums) , nums[0] , nums[0]
        for i in range(1,l):
            if nums[i] > nums[i-1]:
                currsum += nums[i]
            else:
                currsum = nums[i]
            maxsum = max(maxsum,currsum)
        return maxsum