class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sarr = sorted(arr)
        res = []
        #carr = arr.copy()
        ptr = 0
        for i,n in enumerate(arr):
            print(res, "i = ", i,"ptr = ",ptr, "Arr = ",arr[ptr:i+1])
            if sarr[ptr:i+1] != sorted(arr[ptr:i+1]) :
                #print(res,i,sarr[ptr:i+1],sorted(arr[ptr:i]))
                #ptr = i
                continue
            res.append(arr[ptr:i+1])
            #del arr[ptr:i+1]
            #del sarr[ptr:i+1]
            ptr = i + 1  
        if not res : return 1
        return len(res)  