
def checkheight(arr,mid,n):
    count=0
    for i in range(n):
        count=count+int(arr[i]/mid)
    return count
def findmaxheight(arr,n,x,height):
    l=0
    h=height
    ans=-1
    while(l<h):
        mid=int((l+h)/2)
        if checkheight(arr,mid,n)>=x:
            ans=mid
            l=mid+1
        else:
            h=mid-1
    return ans
arr=[12,18,14,9,6]
n=len(arr)
x=6
height=max(arr)
result=findmaxheight(arr,n,x,height)
print("stciks are possible witha height of {0}".format(result))
