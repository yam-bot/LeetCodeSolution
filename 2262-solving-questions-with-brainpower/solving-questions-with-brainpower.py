class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        maxpt = [0] * len(questions)
        def backtrack(i):
            if i >= len(questions):
                return 0
            if maxpt[i]:
                return maxpt[i]
            point, bp = questions[i][0], questions[i][1]
            maxpt[i] = max(backtrack(i+1),point + backtrack(i+bp+1))
            return maxpt[i]
        backtrack(0)
        return max(maxpt)
    