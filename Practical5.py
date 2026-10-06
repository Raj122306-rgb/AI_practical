#water jug
from collections import deque

def is_visited(state, visited):
    return state in visited


def water_jug_bfs():
    max_a, max_b = 5, 4

    visited = set()
    queue = deque()

    queue.append((0, 0))

    while queue:
        a, b = queue.popleft()

        if is_visited((a, b), visited):
            continue

        visited.add((a, b))

        print(f"Jug A: {a}L, Jug B: {b}L")

        if (a == 2 and b == 0) or (a == 0 and b == 2):
            print("Found a solution!")
            return

        possible_states = [
            (max_a, b),
            (a, max_b),
            (0, b),
            (a, 0),

            (min(a + b, max_a),
             b - (min(a + b, max_a) - a)),

            (a - (min(a + b, max_b) - b),
             min(a + b, max_b))
        ]

        for state in possible_states:
            if not is_visited(state, visited):
                queue.append(state)

    print("No solution found!")


water_jug_bfs()
"""
#Travelling salesman

from itertools import permutations

# Distance matrix
dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Number of cities
n = len(dist)

# Cities except starting city 0
cities = range(1, n)

# Set initial minimum distance
min_distance = float('inf')

# Set initial best path
best_path = None

# Generate all possible paths
for path in permutations(cities):

    # Add starting city 0 and ending city 0
    current_path = (0,) + path + (0,)

    # Initialize distance
    distance = 0

    # Calculate total distance
    for i in range(len(current_path) - 1):
        distance += dist[current_path[i]][current_path[i + 1]]

    # Check for minimum distance
    if distance < min_distance:
        min_distance = distance
        best_path = current_path

# Display result
print("Shortest distance:", min_distance)
print("Best path:", best_path)
"""
