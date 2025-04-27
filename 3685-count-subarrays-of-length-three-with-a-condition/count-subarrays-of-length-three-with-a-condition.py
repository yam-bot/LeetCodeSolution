class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        length,count,sub = len(nums), 0, set()
        #for i in range(length):
        #    for j in range(i+1, length):
        #        for k in range(j+1, length):
        #            if (float(nums[i] + nums[k]) == nums[j]/2) and (i,j,k) not in sub:
        #                sub.add((i,j,k))
        #                count += 1
        #                print(nums[i],nums[j],nums[k])
        for i in range(length-2):
            i1,i2,i3 = i, i + 1, i + 2
            if float(nums[i1] + nums[i3]) == nums[i2]/2:
                count += 1
        return count
