class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        num = [0] * 100
        ret = 0
        for x, y in dominoes:
            val = y * 10 + x if x <= y else x * 10 + y 
            ret += num[val]
            num[val] += 1
        return ret

