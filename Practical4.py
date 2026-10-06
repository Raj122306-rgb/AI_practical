#A*
graph = {
    "a": ({"b": 1, "d": 2, "e": 3}, 4),
    "b": ({"d": 1, "c": 2}, 3),
    "c": ({"f": 3}, 2),
    "d": ({"f": 2}, 3),
    "e": ({"f": 4, "d": 3}, 2),
    "f": ({}, 0)
}


def get_min(q):
    mn = (0, 0, float("INF"))

    for i in q:
        if sum(q[i]) < sum(mn):
            mn = (i, q[i][0], q[i][1])

    return mn[0]


def a_star(graph, prev, dst, path, g, pcost):

    print("Connected nodes of current node", prev,
          "with h(n) values:")

    q = {}

    for n in graph[prev][0]:

        if n not in path:

            q[n] = (
                graph[n][1],
                graph[prev][0][n]
            )

            print(n, "->", q[n])

            add1 = sum(q[n])

            path_cost = pcost + add1

            print("A* value for", n, "is:", path_cost)

    while q:

        mn = get_min(q)

        cost = q[mn][1]

        print("Taking minimum vertex:", mn)
        print("-------------------------")

        if dst == mn:
            return path + [dst]

        pc = pcost + cost

        print("Previous path cost:", pc)

        new_path = a_star(
            graph,
            mn,
            dst,
            path + [mn],
            q,
            pc
        )

        if new_path:
            return new_path

    return []


source = input("Enter source vertex: ")
dst = input("Enter destination vertex: ")
heuristic = int(input("Enter heuristic value: "))

path = a_star(
    graph,
    source,
    dst,
    [source],
    heuristic,
    0
)

if path:
    print(path)
else:
    print("Path not found!")

    
#Greedy search
    """
graph = {
    "A": ({"D": 1}, 3),
    "S": ({"A": 2, "E": 3, "D": 2}, 3),
    "E": ({"G": 2}, 5),
    "B": ({"G": 2}, 2),
    "C": ({"G": 3}, 2),
    "D": ({"B": 3, "G": 2}, 4),
    "G": ({}, 0)
}


def greedy_search_rec(graph, prev, dst, path, q):
    print("Connected nodes of current node", prev,
          "with h(n) values:")

    for n in graph[prev][0]:
        if n not in path:
            q[n] = graph[n][1]
            print(n, "->", q[n])

    while q:
        mn = min(q, key=q.get)
        q.pop(mn)

        print("taking minimum h(n) vertex:", mn)

        if dst == mn:
            return path + [dst]

        new_path = greedy_search_rec(
            graph, mn, dst, path + [mn], q
        )

        if new_path:
            return new_path

    return []


source = input("Enter source vertex: ")
dst = input("Enter destination vertex: ")

path = greedy_search_rec(
    graph, source, dst, [source], {}
)

if path:
    print(path)
else:
    print("path not found")
"""
