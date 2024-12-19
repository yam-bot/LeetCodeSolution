class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sarr = sorted(arr)
        res = []
        ptr = 0
        for i,n in enumerate(arr):
            if sarr[ptr:i+1] != sorted(arr[ptr:i+1]) :
                continue
            res.append(arr[ptr:i+1])
            ptr = i + 1  
        if not res : return 1
        return len(res)  