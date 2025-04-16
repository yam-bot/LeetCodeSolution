class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                for k in range(j+1, len(arr)):
                    d1,d2,d3 = abs(arr[i]-arr[j]),abs(arr[j]-arr[k]),abs(arr[i]-arr[k])
                    if d1 <= a and d2 <= b and d3 <= c:
                        count += 1
        return count
