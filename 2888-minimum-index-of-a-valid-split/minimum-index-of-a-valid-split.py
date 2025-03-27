class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        #count = Counter(nums)
        #maxnum = max(nums,key=nums.count)
        countmap = defaultdict(list)
        maxcount,maxnum = 0, 0
        for i,n in enumerate(nums):
            countmap[n].append(i)
            currlen = len(countmap[n])
            if currlen > maxcount:
                maxcount = currlen
                maxnum = n
        #maxcount = count[maxnum]
        subcount,prevcount, lennum = 0, 0, len(nums)
        for i,n in enumerate(nums):
            if n == maxnum:
                subcount += 1
                if subcount > (i + 1) // 2 and maxcount - subcount > (lennum - i -1) // 2:
                    return i
        return -1
         
        