#brute method
import sys
def maxsubarray(arr):
    maxsum=-sys.maxsize
    n=len(arr)
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum+=arr[j]
            if sum>maxsum:
                maxsum=sum
        sum=0
        for k in range(i,-1,-1):
            sum+=arr[k]
            if sum>maxsum:
                maxsum=sum
    return maxsum
arr=[-2,1,-3,4,-1,2,1,-5,4]
arr2=[-1,8,1,-7,-1,5,1,-3]
print("maxsum is: {0}".format(maxsubarray(arr)))
print("maximum sum for 2 is: {0}".format(maxsubarray(arr2)))
            