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
        #n=len(classes)
        #sum=0
        #A=[]
        #for p,q in classes:
        #    sum+=p/q
        #    A.append(((p-q)/(q*(q+1)), p, q)) # change sign
#
        #heapify(A)
#
        #for _ in range(extraStudents):
        #    (r, p, q)=A[0]
        #    if r==0: break
        #    sum-=r # change sign
        #    r2=(p-q)/((q +1.0)* (q + 2.0))
        #    heapreplace(A, (r2, p+1, q+1))
        #    print(A)
        #return sum/n