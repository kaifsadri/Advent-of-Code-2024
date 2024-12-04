M = open("04.input").readlines()
L = dict()
for r, row in enumerate(M):
    for c, letter in enumerate(M[r]):
        L[(r, c)] = letter

p1 = 0
D = set((m, n) for m in {-1, 0, 1} for n in {-1, 0, 1}) - {(0, 0)}
for coord in L:
    if L[coord] == "X":
        for d in D:
            try:
                if (
                    L[(coord[0] + d[0], coord[1] + d[1])] == "M"
                    and L[(coord[0] + d[0] + d[0], coord[1] + d[1] + d[1])] == "A"
                    and L[(coord[0] + d[0] + d[0] + d[0], coord[1] + d[1] + d[1] + d[1])] == "S"
                ):
                    p1 += 1
            except KeyError:
                pass
print(f"Part 1: {p1}")

p2 = 0
D = [
    [(1, 1), (-1, -1)],
    [(-1, 1), (1, -1)],
]
for coord in L:
    if L[coord] == "A":
        try:
            if all(
                L[(coord[0] + d[0][0], coord[1] + d[0][1])] + L[(coord[0] + d[1][0], coord[1] + d[1][1])]
                in {"MS", "SM"}
                for d in D
            ):
                p2 += 1
        except KeyError:
            pass
print(f"Part 2: {p2}")
