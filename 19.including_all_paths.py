def printing_all_paths(path,maze,r,c):
    if r==len(maze)-1 and c==len(maze[0])-1:
        print(path)
        return
    if maze[r][c]==False:
        return
    maze[r][c]=False
    if r<len(maze)-1:
        printing_all_paths(path+' D ',maze,r+1,c)
    if c<len(maze[0])-1:
        printing_all_paths(path+' R ',maze,r,c+1)
    if r>0:
        printing_all_paths(path+' Up ',maze,r-1,c)
    if c>0:
        printing_all_paths(path+' left ',maze,r,c-1)
    maze[r][c]=True
# print("total number of path for 3 rows and 3 columns are :{0}".format(counter(0,0)))
maze=[[True,True,True],
[True,True,True],
[True,True,True]
]
print(len(maze))
printing_all_paths("",maze,0,0)