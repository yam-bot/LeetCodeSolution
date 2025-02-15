class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        l = len(nums)
        if l == 1 : return True
        for i, n in enumerate(nums[0:-1]):
            tempsum = sum(nums[i:i+2])
            if tempsum & 1 != 1:
                return False
        return True
        