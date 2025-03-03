# _ _ _ p _ _ _
# _ _
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less, p, more = [], [], []
        for n in nums:
            if n < pivot:
                less.append(n)
            elif n > pivot:
                more.append(n)
            else:
                p.append(pivot)
        return less + p + more