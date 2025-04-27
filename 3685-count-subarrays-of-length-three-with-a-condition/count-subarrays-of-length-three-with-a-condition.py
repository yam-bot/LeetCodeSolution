class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        length,count,sub = len(nums), 0, set()
        for i in range(length-2):
            if float(nums[i] + nums[i+2]) == nums[i+1]/2:
                count += 1
        return count
