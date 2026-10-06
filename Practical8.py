
import itertools

variables = ["A", "B", "C"]
colors = ["Red", "Blue", "Yellow"]

all_assignments = itertools.product(
    colors,
    repeat=len(variables)
)


def valid(c):
    A, B, C = c

    return (A != B) and (B != C) and (C != A)


solutions = []

for i in all_assignments:
    if valid(i):
        solutions.append(
            dict(zip(variables, i))
        )


print("Valid colorings of the map:")

for sol in solutions:
    print(sol)
