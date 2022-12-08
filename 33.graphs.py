def add_node(vertex):
    if vertex in graph:
        print(vertex," vertex is already present")
    else:
        graph[vertex]=[]
# def add_edge(v1,v2):
#     if v1 not in graph:
#         print(v1," vertex not found")
#     elif v2 not in graph:
#         print(v2," vertex v2 not found")
#     else:
#         graph[v1].append(v2)
#         graph[v2].append(v1)

def add_edge(v1,v2,cost):
    if v1 not in graph:
        print(v1," vertex not found")
    elif v2 not in graph:
        print(v2," vertex v2 not found")
    else:
        list1=[v2,cost]
        list2=[v1,cost]
        graph[v1].append(list1)
        graph[v2].append(list2)
def delete_node(v):
    if v not in graph:
        print(v," vertex not found in graph")
    else:
        graph.pop(v)
        for i in graph.keys():
            list1=graph[i]
            # print(list1)
            for j in list1:
                if v in j:
                    j.clear()
def delete_edge(v1,v2,cost):
    if v1 not in graph:
        print(v1," vertex not found in graph")
    elif v2 not in graph:
        print(v2," vertex not found in graph")
    else:
        temp=[v1,cost]
        temp1=[v2,cost]
        if temp1 in graph[v1]:
            graph[v1].remove(temp1)
            graph[v2].remove(temp)
graph={}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_node("F")
add_node("G")
add_edge("A","B",10)
add_edge("B","E",14)
add_edge("A","C",5)
add_edge("A","D",19)
add_edge("B","D",13)    
add_edge("C","D",1)
add_edge("E","D",2)
print(graph)
print("after deletion")
delete_edge("C","D",1)
print(graph)
# delete_node("C")
# print("after deletion")
# print(graph)