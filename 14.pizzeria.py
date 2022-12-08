def  binary_search(arr,x):
    low=0
    high=len(arr)-1
    key=-1
    while low<=high:
        mid=(high+low)//2
        if arr[mid]<x:
            key=mid
            low=mid+1
        elif arr[mid]>x:
            high=mid-1
        else:
            return arr[mid]
    return arr[key]
arr=[10,12,14,16,19]
print(binary_search(arr,15))

