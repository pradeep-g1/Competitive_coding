def lcs(str1,str2):
    if len(str1)==0 or len(str2)==0:
        return 0
    if str1[0]==str2[0]:
        return 1+lcs(str1[1::],str2[1::])
    return max(lcs(str1[1::],str2),lcs(str1,str2[1::]))
str1="AEETAB"
str2="EWTWAYB"
print("the longest common subsequence is: ",lcs(str1,str2))