#alpha beta search
"""
tree = {
    'A': ['B', 'C'],
    'B': [3, 5],
    'C': [6, 9]
}

def minimax_alpha_beta(node, depth, alpha, beta, max_player):

    if depth == 0:
        if node in tree:
            return tree[node][0] if max_player else tree[node][0]
        else:
            return node

    if max_player:
        value = float('-inf')

        for child in tree[node]:
            value = max(
                value,
                minimax_alpha_beta(
                    child,
                    depth - 1,
                    alpha,
                    beta,
                    False
                )
            )

            alpha = max(alpha, value)

            if alpha >= beta:
                print("Pruning branch at node", node)
                break

        return value

    else:
        value = float('inf')

        for child in tree[node]:
            value = min(
                value,
                minimax_alpha_beta(
                    child,
                    depth - 1,
                    alpha,
                    beta,
                    True
                )
            )

            beta = min(beta, value)

            if beta <= alpha:
                print("Pruning branch at node", node)
                break

        return value


best_score = minimax_alpha_beta(
    'A',
    1,
    float('-inf'),
    float('inf'),
    True
)

print(f"The best score is: {best_score}")
"""
#Hill climb
import random

distance = [
    [0, 2, 9, 10],
    [2, 0, 6, 4],
    [9, 6, 0, 3],
    [10, 4, 3, 0]
]

def get_cost(tour):
    cost = 0
    for i in range(len(tour)):
        cost += distance[tour[i-1]][tour[i]]
    print("cost of tour:", cost)
    return cost


def get_neighbour(tour):
    a, b = random.sample(range(len(tour)), 2)
    tour[a], tour[b] = tour[b], tour[a]
    return tour


def hill_climb():
    current = [0, 1, 2, 3]
    random.shuffle(current)

    current_cost = get_cost(current)

    print("Starting tour:", current, "cost:", current_cost)

    for i in range(10):
        neighbour = current[:]

        print("Current neighbour:", neighbour)

        neighbour = get_neighbour(neighbour)

        print("Connected neighbour:", neighbour)

        neighbour_cost = get_cost(neighbour)

        if neighbour_cost < current_cost:
            current = neighbour
            print("Current neighbour:", current)

            current_cost = neighbour_cost

            print("Current cost:", current_cost)

            print("Better tour found:", current, "cost:", current_cost)

        else:
            print("No better neighbour found")

    return current, current_cost


best_tour, best_cost = hill_climb()

print("\nBest tour:", best_tour)
print("Best cost:", best_cost)
