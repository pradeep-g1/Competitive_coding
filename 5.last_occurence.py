# def l_occurence(arr,target,i):
#     if i==len(arr):
#         return 
#     l_occurence(arr,target,i+1)
#     print(arr[i],end=" ")
# arr=[3,5,7,4,5,6,7,9,12]
# l_occurence(arr,5,0)

def l_occurence(arr,target,i):
    if i==len(arr):
        return 
    if arr[len(arr)-i-1]==target:
        return len(arr)-i-1
    else:
        return l_occurence(arr,target,i+1)
arr=[3,5,7,4,5,6,3,7,9,12]
print("at the index is:",l_occurence(arr,3,0))