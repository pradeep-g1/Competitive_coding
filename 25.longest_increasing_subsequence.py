def lis(arr,n):
    lis=[1]*n
    for i in range(1,n):
        for j in range(i):
            if arr[i]>arr[j] and lis[i]<lis[j]+1:
                lis[i]=lis[j]+1
    return max(lis)
arr=[10,22,9,33,21,50,41,60]
n=len(arr)
print("Total length is: {0}".format(lis(arr,n)))