def maximum_subarray(arr):
    maxsum=arr[0]
    sum=0
    for i in arr:
        if sum<0:
            sum=0
        sum+=i
        maxsum=max(maxsum,sum)
    return maxsum
arr=[-1,8,1,-7,-1,5,1,-3]
print("maximum sum of subarray is: {0}".format(maximum_subarray(arr)))
