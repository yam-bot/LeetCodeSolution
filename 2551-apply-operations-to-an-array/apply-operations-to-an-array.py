class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        intarr , zeroarr = [] , []
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
            if nums[i]:
                intarr.append(nums[i])
            else:
                zeroarr.append(nums[i])
        if nums[-1] : intarr.append(nums[-1])
        else : zeroarr.append(nums[-1])
        return (intarr+zeroarr)