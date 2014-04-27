def solution(N, A):
    # write your code in Python 2.6
    cntrs = [0] * N
    maxVal = 0
    rstVal = 0
    for k in range(len(A)):
        if A[k] == N + 1:
            rstVal = maxVal
        else:
            if rstVal >= cntrs[A[k]-1]:
                cntrs[A[k]-1] = rstVal + 1
                maxVal = max(maxVal,rstVal + 1)
            else:
                cntrs[A[k]-1] = cntrs[A[k]-1] + 1
                maxVal = max(maxVal,cntrs[A[k]-1])
        # print cntrs
        # print rstVal, maxVal

    for k in range(len(cntrs)):
        if rstVal > cntrs[k-1]:
                cntrs[k-1] = rstVal
        # print cntrs
    return cntrs

# GET INPUT AND SETUP ARRAY, N
import random
N = int(raw_input('N--> '))
M = int(raw_input('M--> '))
A = [0] * M
for i in range(M):
   A[i-1]=random.randint(1,N+1)

print A
print solution(N,A)
# END OF GET INPUT, REMOVE LINES ABOVE


