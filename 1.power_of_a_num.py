def power(x,n):
    if n!=0:
        return x*power(x,n-1)
    else:
        return 1
x=int(input("enter the base: "))
n=int(input("enter the exponent: "))
print(power(x,n))