# Setup:
R = {(1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1), (0, 1): (1, 0)}
M = dict()  # where obstacles are
for r, row in enumerate(open("06.input").readlines()):
    for c, item in enumerate(row.strip()):
        M[(r, c)] = item
        if item == "^":
            initloc = (r, c)
d = (-1, 0)  # point up


# Part 1:
p = initloc
been = {initloc}
while True:
    np = (p[0] + d[0], p[1] + d[1])
    if np not in M:
        break
    elif M[np] == "#":
        d = R[d]
    else:
        p = np
        been.add(p)
print(f"Part 1: {len(been)}")


# Part 2:
def isloopy(pos, direction):
    global M, R, B
    p = pos
    d = direction
    b = {(p, d)}
    while True:
        np = (p[0] + d[0], p[1] + d[1])
        if np not in M:
            return False
        elif M[np] == "#":
            d = R[d]
        else:
            if (np, d) in b or (np, d) in B:
                return True
            else:
                p = np
                b.add((p, d))


p = initloc
d = (-1, 0)  # point up
p2 = 0
B = set()
been.clear()
while True:
    B.add((p, d))
    been.add(p)
    np = (p[0] + d[0], p[1] + d[1])
    if np not in M:
        break
    elif M[np] == "#":
        d = R[d]
    else:
        if np not in been:  # cannot add obstacle on the path the guard already taken
            M[np] = "#"
            if isloopy(p, d):
                p2 += 1
            M[np] = "."
        p = np
print(f"Part 2: {p2}")
