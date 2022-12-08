def counter(r,c):
    if r==1 or c==1:
        return 1
    left = counter(r-1,c)
    right = counter(c-1,r)
    return left+right
def printing_paths(path,r,c):
    if r==1 and c==1:
        print(path)
        return
    if r>1 and c>1:
        printing_paths(path+'d',r-1,c-1)
    if r>1:
        printing_paths(path+'D',r-1,c)
    if c>1:
        printing_paths(path+'R',r,c-1)
print("total number of path for 3 rows and 3 columns are :{0}".format(counter(3,3)))
printing_paths("",3,3)