class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for operation in range(k):
            minnum = min(nums)
            ind = nums.index(minnum)
            nums[ind] = minnum * multiplier
        return nums
        