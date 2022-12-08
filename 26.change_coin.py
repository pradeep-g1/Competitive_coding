def coin_change(coins,num_of_denominations,value):
    if value==0:
        return 1
    if value<0:
        return 0
    if num_of_denominations<=0 and value>=1:
        return 0
    include_deno=coin_change(coins,num_of_denominations,value-coins[0])
    print(include_deno,end=" ")
    not_include_deno=coin_change(coins[1:],num_of_denominations-1,value)
    return include_deno+not_include_deno
coins=[1,2,3]
value=4
print("possible ways: ",coin_change(coins,len(coins),value))