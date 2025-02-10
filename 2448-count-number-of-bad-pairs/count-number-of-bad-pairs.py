class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        diffcount = defaultdict(int)
        badpairs = 0
        for i in range(len(nums)):
            diff = nums[i] - i
            badpairs += i - diffcount.get(diff,0)
            diffcount[diff] += 1
        return badpairs