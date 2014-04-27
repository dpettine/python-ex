def solution(R, X, M):
    # write your code in Python 2.6
    if (2*X*len(R))>M:
        return -1
    else:
        bar=0
        term=0
        dstMax=0
        dstVect=[]
        orig = 0
        cont=1
        for i in range(len(R)):
            if (R[i]-term)<X:
                bar = int((bar + R[i])/cont)
                l = 2*X*(cont)
                term = max(bar+int(l/2),orig+l)
                dstMax = abs(term-X-R[i])
                cont = cont+1
            else:
                orig = term
                term = R[i] + X
                cont = 1
		bar = R[i]
                dstVect.append(dstMax)
        return max(dstVect)

R=[1,3,5,14]
X = 2
M = 16
print solution(R,X,M)
