from collections import Counter

G = dict()
for r, row in enumerate(open("12.input").readlines()):
    for c, t in enumerate(row.strip()):
        G[(r, c)] = t
A = dict()  # partitioning the areas
D = {(-1, 0), (1, 0), (0, 1), (0, -1)}
while G:
    p, t = G.popitem()
    A[p] = {p}
    togo = {
        (p[0] + d[0], p[1] + d[1])
        for d in D
        if (p[0] + d[0], p[1] + d[1]) in G and G[(p[0] + d[0], p[1] + d[1])] == t
    }
    A[p] |= togo
    while togo:
        G.pop(pp := togo.pop())
        togo |= {
            (pp[0] + d[0], pp[1] + d[1])
            for d in D
            if (pp[0] + d[0], pp[1] + d[1]) in G and G[(pp[0] + d[0], pp[1] + d[1])] == t
        }
        A[p] |= togo

# Part 1: sum up the perimeter of each area
P = Counter()
for p in A:
    for pp in A[p]:
        s = {(pp[0] + d[0], pp[1] + d[1]) for d in D if (pp[0] + d[0], pp[1] + d[1]) in A[p]}
        P[p] += 4 - len(s)
print(f"Part 1: {sum(len(A[n]) * P[n] for n in A)}")

# Part 2: count the corners of each area (corners = sides)
P = Counter()
D = [{(-1, 0), (0, 1)}, {(0, 1), (1, 0)}, {(1, 0), (0, -1)}, {(0, -1), (-1, 0)}]
for p in A:
    for pp in A[p]:
        for c1, c2 in D:
            if (pp[0] + c1[0], pp[1] + c1[1]) not in A[p] and (pp[0] + c2[0], pp[1] + c2[1]) not in A[p]:
                P[p] += 1
            elif (
                (pp[0] + c1[0], pp[1] + c1[1]) in A[p]
                and (pp[0] + c2[0], pp[1] + c2[1]) in A[p]
                and (pp[0] + c1[0] + c2[0], pp[1] + c1[1] + c2[1]) not in A[p]
            ):
                P[p] += 1
print(f"Part 2: {sum(len(A[n]) * P[n] for n in A)}")
