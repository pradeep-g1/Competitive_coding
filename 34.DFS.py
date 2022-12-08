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

def add_edge(v1,v2):
    if v1 not in graph:
        print(v1," vertex not found")
    elif v2 not in graph:
        print(v2," vertex v2 not found")
    else:
        #list1=[v2,cost]
        #list2=[v1,cost]
        graph[v1].append(v2)
        graph[v2].append(v1)

def dfs(node,visited,graph):
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            dfs(i,visited,graph)


visited=set()
graph={}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_node("F")
add_node("G")
add_edge("A","B")
add_edge("B","E")
add_edge("A","C")
add_edge("A","D")
add_edge("B","D")    
add_edge("C","D")
add_edge("E","D")
print(graph)
print("traversal: ")
dfs("A",visited,graph)