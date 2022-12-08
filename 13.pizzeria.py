def closest(arr,left,right,target):
    if arr[-1]<target:
        print("{0} is the amount spending".format(arr[-1]))
    elif arr[0]>target:
        print("{0} is the amount spending".format(arr[0]))
    else:
        mid=int((left+right)/2)
        if arr[mid]==target:
            print("{0} is the amount spending".format(arr[mid]))
        else:
            if arr[mid]>target:
                if target > arr[mid-1] and target < arr[mid]:
                    x=abs(target-arr[mid-1])
                    y=abs(target-arr[mid])
                    if x < y:
                        print("{0} is the amount spending".format(arr[mid-1]))
                    else:
                        print("{0} is the amount spending".format(arr[mid]))
                else:
                    return closest(arr,left,mid-1,target)
            elif arr[mid]<target:
                if target > arr[mid] and target < arr[mid+1]:
                    x=abs(target-arr[mid])
                    y=abs(target-arr[mid+1])
                    if x<y:
                        print("{0} is the amount spending".format(arr[mid]))
                    else:
                        print("{0} is the amount spending".format(arr[mid+1]))
                else:
                    return closest(arr,mid+1,right,target)
def money_spending(arr):
    money_spent=[]
    for i in range(len(arr)):
        sum=0
        for j in range(i+1):
            sum=sum+arr[j]
        money_spent.append(sum)
    return money_spent
arr=[10,2,6,4,1]
target=19
money_spent=money_spending(arr)
left=0
right=len(arr)
closest(money_spent,left,right,target)
