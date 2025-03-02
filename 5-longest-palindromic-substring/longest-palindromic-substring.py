class Solution:
    def longestPalindrome(self, s: str) -> str:
        start ,end, n = 0, 0, len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            if (i+1) <= (n-1) and s[i] == s[i+1]:
                dp[i][i+1] = True
                start , end = i, i+1
        for diff in range(2,n):
            for i in range(n-diff):
                j = i + diff
                if s[i] == s[j] and dp[i+1][j-1] == True:
                    dp[i][j] = True
                    start, end = i, j
        return s[start:end+1]