from collections import Counter

G = dict()
for r, row in enumerate(open("12.input").readlines()):
    for c, t in enumerate(row.strip()):
        G[r + c * 1j] = t
A = dict()  # partitioning the areas
D = {-1 + 0j, 1 + 0j, 0 + 1j, 0 - 1j}
while G:
    p, t = G.popitem()
    A[p] = {p}
    togo = {p + d for d in D if p + d in G and G[p + d] == t}
    A[p] |= togo
    while togo:
        G.pop(pp := togo.pop())
        togo |= {pp + d for d in D if pp + d in G and G[pp + d] == t}
        A[p] |= togo

# Part 1: sum up the perimeter of each area
P = Counter()
for p in A:
    for pp in A[p]:
        P[p] += 4 - len({pp + d for d in D if pp + d in A[p]})
print(f"Part 1: {sum(len(A[n]) * P[n] for n in A)}")

# Part 2: count the corners of each area (corners = sides)
P = Counter()
D = [{-1 + 0j, 0 + 1j}, {0 + 1j, 1 + 0j}, {1 + 0j, 0 - 1j}, {0 - 1j, -1 + 0j}]
for p in A:
    for pp in A[p]:
        for c1, c2 in D:
            if pp + c1 not in A[p] and pp + c2 not in A[p]:
                P[p] += 1
            elif pp + c1 in A[p] and pp + c2 in A[p] and pp + c1 + c2 not in A[p]:
                P[p] += 1
print(f"Part 2: {sum(len(A[n]) * P[n] for n in A)}")
