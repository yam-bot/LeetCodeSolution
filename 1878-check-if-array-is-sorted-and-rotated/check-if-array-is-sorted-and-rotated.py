class Solution:
    def check(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        for i in range(len(nums)):
            if sorted_nums[i:] == nums:
                return True
            sorted_nums.append(sorted_nums[i])
        return False
