def solution(A):
    tot = sum(A)
    lSum = 0
    minDiff = abs(tot)
    for i in range(len(A)):
        lSum = lSum + A[i]
        if abs(tot - 2 * lSum) < minDiff:
            minDiff = abs(tot - 2 * lSum)
    return minDiff
A = [5000, 3000]
print solution(A)
