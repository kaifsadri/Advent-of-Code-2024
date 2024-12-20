Track = set()
S = 0
E = 0
for row, line in enumerate(open("20.input").readlines()):
    for col, item in enumerate(line):
        if item == "." or item == "S" or item == "E":
            Track.add(complex(row, col))
        if item == "S":
            S = complex(row, col)
        if item == "E":
            E = complex(row, col)
# now for a linear track representation
T = {0: S}
R = {S: 0}
loc = S
step = 0
while loc != E:
    for d in {1, -1, 1j, -1j}:
        if loc + d in Track and loc + d not in R:
            T[step + 1] = loc + d
            R[loc + d] = step + 1
            loc += d
            break
    step += 1


# Part 1: check all poinst in 2 manhattan distance
P1 = 0
ch_range = {2, -2, 2j, -2j}
for n in range(step + 1 - 102):
    t = T[n]
    for d in ch_range:
        try:
            P1 += R[t + d] - n >= 100 + 2
        except KeyError:
            pass
print(f"Part 1: {P1}")

# Part 2: extend search range to 20 manhattan distance
P2 = 0
ch_range = set(
    complex(r, i)
    for r in range(-20, 21)
    for i in range(-20 + abs(r), 21 - abs(r))
    if abs(r) + abs(i) <= 20
)
for n in range(step + 1 - 102):
    t = T[n]
    for d in ch_range:
        try:
            P2 += R[t + d] - n >= 100 + abs(d.real) + abs(d.imag)
        except KeyError:
            pass
print(f"Part 2: {P2}")
