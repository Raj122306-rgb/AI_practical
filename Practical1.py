#DFS
"""
graph ={
    'A' : ['B','D'],
    'B' : ['C','F'],
    'C' : ['E','G','H'],
    'G' : ['F','H'],
    'E' : ['B','F'],
    'F' : ['A'],
    'D' : ['F'],
    'H' : ['A']

    }
def dfs(g,n,seen,d):
    if n not in seen:
        seen.append(n)
        for i in g[n]:
            if seen [-1] == d:
                break
            dfs(g,i,seen,d)
        return seen

print(dfs(graph,'A',[],'H'))
"""
#BFS
import collections


# BFS Graph Traversal
def bfs(graph, root):
    seen = set([root])
    queue = collections.deque([root])

    while queue:
        vertex = queue.popleft()
        visit(vertex)

        for node in graph[vertex]:
            if node not in seen:
                seen.add(node)
                queue.append(node)


# Find all paths
def all_path(cst, end, graph):
    todo = [(cst, [cst])]

    while len(todo):
        node, path = todo.pop(0)

        for next_node in graph[node]:

            if next_node in path:
                continue

            if next_node == end:
                print("Ideal solution")
                yield path + [next_node]

            else:
                todo.append(
                    (next_node, path + [next_node])
                )


# Visit function
def visit(n):
    print(n)


# BFS Shortest Path
def bfs_shortest_path(graph, source, destination):

    checked = []
    queue = [[source]]

    if source == destination:
        return "SOURCE IS DESTINATION"

    while queue:

        path = queue.pop(0)
        node = path[-1]

        if node not in checked:

            neighbours = graph[node]

            for neighbour in neighbours:

                new_path = list(path)
                new_path.append(neighbour)

                queue.append(new_path)

                if neighbour == destination:
                    return new_path

            checked.append(node)

    return "PATH DOES NOT EXIST"


# Graph
graph = {
    'A': ['B', 'D'],
    'B': ['C', 'F'],
    'C': ['E', 'G', 'H'],
    'G': ['E', 'H'],
    'E': ['B', 'F'],
    'F': ['A'],
    'D': ['F'],
    'H': ['A']
}


# Graph Traversal
print("GRAPH TRAVERSAL:")
bfs(graph, 'A')


# All Paths
print("\nAll paths:")

for x in all_path('A', 'E', graph):
    print(x)


# Shortest Path
print("\nSHORTEST PATH OF GRAPH IS:")

print(bfs_shortest_path(graph, 'A', 'E'))
