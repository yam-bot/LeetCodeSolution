class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        l = len(nums)
        ans = 0
        productdict = defaultdict(int)
        for i in range(l):
            for j in range(i+1,l):
                    prod = nums[i] * nums[j]
                    ans += 8 * productdict[prod]
                    productdict[prod] += 1
        return ans
