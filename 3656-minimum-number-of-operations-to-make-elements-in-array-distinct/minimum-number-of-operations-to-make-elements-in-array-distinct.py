class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums_set, op = set(nums), 0
        while len(nums_set) != len(nums):
            if len(nums) < 3:
                nums = []
            else:
                nums = nums[3:]
            op += 1
            nums_set = set(nums)
        return op