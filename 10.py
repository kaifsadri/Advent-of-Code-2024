from collections import defaultdict

G = dict()
Z = set()  # all the 0's
N = set()  # all the 9's
for r, row in enumerate(open(f"10.input")):
    for c, h in enumerate(row.strip()):
        G[r, c] = (n := int(h))
        if 0 == n:
            Z.add((r, c))
        if 9 == n:
            N.add((r, c))
D = [(-1, 0), (0, -1), (0, 1), (1, 0)]


# for part 1, find out how many zeros each nine leads to
def zeros(n):
    global G
    if G[n] == 0:
        return {n}
    S = set()
    togo = {
        (n[0] + d[0], n[1] + d[1])
        for d in D
        if (n[0] + d[0], n[1] + d[1]) in G and G[(n[0] + d[0], n[1] + d[1])] == G[n] - 1
    }
    if len(togo) == 0:
        return set()
    for p in togo:
        S |= zeros(p)
    return S


print(f"Part 1: {sum(len(zeros(niner)) for niner in N)}")


# part 2: find out how many paths you have to each nine
def paths(z):
    global G
    if G[z] == 9:
        return 1
    togo = {
        (z[0] + d[0], z[1] + d[1])
        for d in D
        if (z[0] + d[0], z[1] + d[1]) in G and G[(z[0] + d[0], z[1] + d[1])] == G[z] + 1
    }
    if len(togo) == 0:
        return 0
    return sum(paths(p) for p in togo)


print(f"Part 2: {sum(paths(z) for z in Z)}")
