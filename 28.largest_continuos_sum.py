import sys
def maximum_sum(arr):
    maximum_so_far=-sys.maxsize
    maximum_ending_here=0
    for i in range(len(arr)):
        maximum_ending_here=maximum_ending_here+arr[i]
        if maximum_so_far<maximum_ending_here:
            maximum_so_far=maximum_ending_here
        if maximum_ending_here<0:
            maximum_ending_here=0
    return maximum_so_far
# arr=[-2,-3,4,-1,-2,1,5,3]
arr=[1,-2,4,3]
print("Maximum sum is: {0}".format(maximum_sum(arr)))

