def make_pairs(start,end):
    timings=[]
    for i in range(len(start)):
        temp=[]
        temp.append(start[i])
        temp.append(end[i])
        timings.append(temp)
    for i in timings:
        print(i,end=" ")
def timings_list(start,end):
    timings=[]
    for i in range(len(start)):
        timings.append([start[i],end[i]])
    return timings
start=[2,4,5,9,20]
end=[3,5,7,10,30]
make_pairs(start,end)
timings=timings_list(start,end)
print("\nthe timings list is: ",timings)
arrival_time=18
i=0
n=len(start)
time=timings[0][0]
while arrival_time>time and i+1<n:
    time=timings[i+1][0]
    i=i+1
# print(time)
# print(timings[i])
if timings[i][0]>arrival_time and timings[i-1][1]<arrival_time:
    print("{0} hours waiting".format(timings[i][0]-arrival_time))
elif arrival_time==timings[i-1][1]:
    print("{0} hours waiting".format(timings[i][0]-arrival_time))
else:
    print("{0} hours waiting".format(-1))