def func(A):
   maxDst=0
   for i in range(len(A)):
      for j in range( i+max(1,maxDst), len(A) ):
          if A[j]>=A[i] and j-i>maxDst:
              maxDst = j - i
   return maxDst


lst = [ 4,3,4,6,2,5  ]
print func(lst) 
