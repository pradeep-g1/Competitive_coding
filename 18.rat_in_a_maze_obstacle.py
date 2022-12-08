def counter(r,c):
    if r==2 or c==2:
        return 1
    left = counter(r+1,c)
    right = counter(c+1,r)
    return left+right
def printing_paths(path,maze,r,c):
    if r==len(maze)-1 and c==len(maze[0])-1:
        print(path)
        return
    if maze[r][c]==False:
        return
    if r<len(maze)-1:
        printing_paths(path+'D',maze,r+1,c)
    if c<len(maze[0])-1:
        printing_paths(path+'R',maze,r,c+1)
print("total number of path for 3 rows and 3 columns are :{0}".format(counter(0,0)))
maze=[[True,True,True],
[True,False,True],
[False,True,True]
]
print(len(maze))
printing_paths("",maze,0,0)