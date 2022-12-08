def fibo(n):
    if n in [0,1]:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
num=int(input("enter the num: "))
res=[]
for i in range(num+1):
    res.append(fibo(i))
print(res[-1])