class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        num_set = set()
        for n in nums:
            if n < k:
                return -1
            elif n > k:
                num_set.add(n)
        return len(num_set)
