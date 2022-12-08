def closest(arr,left,right,target):
    if arr[-1]<target:
        print("{0} is the closest element in the array".format(arr[-1]))
    elif arr[0]>target:
        print("{0} is the closest element in the array".format(arr[0]))
    else:
        mid=int((left+right)/2)
        if arr[mid]==target:
            print("{0} is the closest element in the array".format(arr[mid]))
        else:
            if arr[mid]>target:
                if target > arr[mid-1] and target < arr[mid]:
                    x=abs(target-arr[mid-1])
                    y=abs(target-arr[mid])
                    if x < y:
                        print("{0} is the smallest element in the array".format(arr[mid-1]))
                    else:
                        print("{0} is the smallest element in the array".format(arr[mid]))
                else:
                    return closest(arr,left,mid-1,target)
            elif arr[mid]<target:
                if target > arr[mid] and target < arr[mid+1]:
                    x=abs(target-arr[mid])
                    y=abs(target-arr[mid+1])
                    if x<y:
                        print("{0} is the smallest element in the array".format(arr[mid]))
                    else:
                        print("{0} is the smallest element in the array".format(arr[mid+1]))
                else:
                    return closest(arr,mid+1,right,target)
arr=[1,2,2,3,6,6,9,10,14]
closest(arr,0,len(arr),11)
                    