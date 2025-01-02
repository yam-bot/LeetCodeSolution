class Solution:
    def maxScore(self, s: str) -> int:
        maxcombo = 0
        s = [int(n) for n in s]
        if 1 not in s : return (s.count(0) -1)
        if 0 not in s : return (s.count(1) - 1)
        for i in range(len(s)-1):
            c = s[0:i+1].count(0) + s[i+1:].count(1)
            print(s[0:i+1],s[i+1:],c)
            maxcombo = max(maxcombo,c)
        return maxcombo