# def printarray(arr,n,i):
#     if i==n:
#         return
#     else:
#         print(arr[i],end=" ")
#         printarray(arr,n,i+1)
# arr=[10,12,3,4,23]
# printarray(arr,len(arr),0)
# print()

def f_occurence(arr,i,target):
    if i==len(arr):
        return "Not found"
    elif target==arr[i]:
        return i
    else:
        return f_occurence(arr,i+1,target)
arr=[1,2,3,2,3,4,6,5,3]
print(f_occurence(arr,0,4))