# def fibo(n):
#     arr=[]
#     arr.append(0)
#     arr.append(1)
#     arr.append(1)
#     for i in range(3,n+2):
#         arr.append((arr[i-1]+arr[i-2]))
#     return arr
# n=int(input("enter the num: "))
# res=fibo(n)
# for i in res:
#     print(i,end=" ")

def fibo(n,arr):
    arr[0]=0
    arr[1]=1
    arr[2]=1
    for i in range(3,n+2):
        arr[i]=arr[i-1]+arr[i-2]
    return arr
n=int(input("enter the num: "))
arr=[-1]*(n+2)
res=fibo(n,arr)
for i in res:
    print(i,end=" ")
print()

