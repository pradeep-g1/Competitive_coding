def decoding_helper(string):
    if len(string)==0 or (len(string)==1 and string[0]=="0"):
        return 0
    return possible_decodings(string,len(string))
def possible_decodings(string,n):
    if n==0 or n==1:
        return 1
    count=0
    if string[n-1]>"0":
        count=possible_decodings(string,n-1)
    if (string[n-2]=='1' or string[n-2]=='2') and string[n-1]<'7':
        count+=possible_decodings(string,n-2)
    return count
string="141213"
print("The possible decodings of a given string is: {0}".format(decoding_helper(string))) 