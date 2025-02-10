class Solution:
    def clearDigits(self, s: str) -> str:
        l = len(s)
        digitInd = [i for i in range(l) if s[i].isdigit()]
        s = list(s)
        cnt = 0
        for i in digitInd:
            if i > 2 and cnt >0:
                i -= cnt
            del s[i-1:i+1]
            cnt += 2
        s = "".join(s)
        return s
        