class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count, prev = 0, nums[0]
        for i in range(1,len(nums)-1):
            if prev == nums[i] :
                continue
            l, r = i-1, i+1
            while nums[r] == nums[i] and r < len(nums)-1:
                r += 1
            if (nums[l] < nums[i] and nums[r] < nums[i]) or (nums[l] > nums[i] and nums[r] > nums[i]):
                count += 1
            prev = nums[i]
        return count