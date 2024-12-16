class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        ratioStudent = []
        sumratio = 0
        for np,tot in classes:
            newratio = (np + 1)/(tot +1)
            ratio = np / tot
            ratioStudent.append((-(newratio - ratio), np, tot))
            sumratio += ratio
        heapify(ratioStudent)

        for i in range(extraStudents):
            (d,p,t) = ratioStudent[0]
            newr = (p + 2)/(t + 2)
            oldr = (p + 1) / (t + 1)
            sumratio -= d
            heapreplace(ratioStudent,(-(newr - oldr),p+1,t+1))
        return sumratio/len(classes)