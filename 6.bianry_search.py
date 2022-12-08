def binary_search(arr,left,right,value):
    if right>=left:
        mid=int((right+left)/2)
        if arr[mid]==value:
            print("{0} is found in the array".format(value))
        elif arr[mid]<value:
            return binary_search(arr,mid+1,right,value)
        elif arr[mid]>value:
            return binary_search(arr,left,mid-1,value)
    else:
        print("{0} value is not found in the array".format(value))

arr=[5,3,2,9,12,16,18,22]
arr.sort()
binary_search(arr,0,len(arr),22)