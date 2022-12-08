def traverse_m(arr,cur_row,cur_col):
    m=len(arr[0])
    n=len(arr)
    if cur_col>=m:
        return 0
    if cur_row>=n:
        return 1
    print(arr[cur_row][cur_col],end=" ")
    if traverse_m(arr,cur_row,cur_col+1)==1:
        return 1
    print()
    return traverse_m(arr,cur_row+1,0)


arr=[[1,2,3],
[4,5,6],
[7,8,9]]
traverse_m(arr,0,0)