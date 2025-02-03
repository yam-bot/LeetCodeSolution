class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1 : return 1
        maxlen , dec , inc = 0 , 1 , 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1] :
                inc += 1
                dec = 1
            elif nums[i] < nums[i-1]:
                inc = 1
                dec += 1
            else:
                inc = dec = 1
            maxlen = max(maxlen,inc,dec)
        return maxlen
            