# [-4, -1, -1, 0, 1, 2]
#    i   l            r
#    i       l        r
#    i          l     r
#    i             l  r
#    i            

#  l    i            r
#       l   i        r
#       l      i     r
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue
            left, right = i+1,  len(nums)-1
            while left < right:
                if i == left:
                    left += 1
                elif i == right:
                    right -= 1
                sumthree = n + nums[left] + nums[right]
                #print(nums[left],nums[i],nums[right])
                if sumthree < 0:
                    left += 1
                elif sumthree > 0 :
                    right -= 1
                else:
                    ans.append([n,nums[left],nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
        return ans