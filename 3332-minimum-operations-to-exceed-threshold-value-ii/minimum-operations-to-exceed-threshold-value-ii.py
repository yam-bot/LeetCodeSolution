class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        ops = 0
        while nums[0] < k:
            x , y = heappop(nums) , heappop(nums)
            newnum = (min(x,y) * 2 ) + max(x,y)
            heappush(nums,newnum)
            #print(nums)
            ops += 1
        return ops

            
        