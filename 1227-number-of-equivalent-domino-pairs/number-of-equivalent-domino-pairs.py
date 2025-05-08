class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        l = len(dominoes)
        cnt = 0
        #for i, d1 in enumerate(dominoes):
        #    for d2 in dominoes[i+1:l]:
        #        if (d1[0] == d2[1] and d1[1] == d2[0]) or (d1[0] == d2[0] and d1[1] == d2[1]):
        #            cnt += 1
        #return cnt
        #num = [0] * 100
        #ret = 0
        #for x, y in dominoes:
        #    val = x * 10 + y if x <= y else y * 10 + x
        #    ret += num[val]
        #    num[val] += 1
        #    print("val",val,"num",num[val],"ret",ret)
        num = [0] * 100
        ret = 0
        for x, y in dominoes:
            val = y * 10 + x if x <= y else x * 10 + y 
            ret += num[val]
            num[val] += 1
        return ret

