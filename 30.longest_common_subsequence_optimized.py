def lcs(str1,str2):
    m=len(str1)
    n=len(str2)
    dp=[[0 for i in range(n+1)] for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif str1[m-i]==str2[n-j]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]
str1="AEETAB"
str2="EWTWAYB"
print("length of lcs is: {0}".format(lcs(str1,str2)))