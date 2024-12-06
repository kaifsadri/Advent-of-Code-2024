M = list(list(line.strip()) for line in open("06.input").readlines())
R = {(1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1), (0, 1): (1, 0)}

# Part 1:
been = set()
d = (-1, 0)  # point up
for row in range(len(M)):
    for col in range(len(M[0])):
        if M[row][col] == "^":
            initloc = (row, col)

p = initloc
while True:
    been.add(p)
    np = (p[0] + d[0], p[1] + d[1])
    if not (0 <= np[0] < len(M) and 0 <= np[1] < len(M[0])):
        break
    elif M[np[0]][np[1]] == "#":
        d = R[d]
    else:
        p = np
print(f"Part 1: {len(been)}")


# Part 2:
def isloopy(pos, direction):
    global M, R, B
    p = pos
    d = direction
    b = {(p, d)}
    while True:
        np = (p[0] + d[0], p[1] + d[1])
        if not (0 <= np[0] < len(M) and 0 <= np[1] < len(M[0])):
            return False
        elif M[np[0]][np[1]] == "#":
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
    if not (0 <= np[0] < len(M) and 0 <= np[1] < len(M[0])):
        break
    elif M[np[0]][np[1]] == "#":
        d = R[d]
    # else:  # here is a valid step, so we have the choice of plugging it and checking for loopiness
    else:
        if np not in been:  # cannot add obstacle on the path the guard already taken
            M[np[0]][np[1]] = "#"
            if isloopy(p, d):
                p2 += 1
            M[np[0]][np[1]] = "."
        p = np
print(f"Part 2: {p2}")
